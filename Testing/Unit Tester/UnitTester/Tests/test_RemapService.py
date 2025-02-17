import sys
from collections import defaultdict
import unittest.mock as mock
import ntpath
from typing import Optional

from .baseFileUnitTest import BaseFileUnitTest
from ..src.Config import Configs
from ..src.constants.ConfigKeys import ConfigKeys

sys.path.insert(1, Configs[ConfigKeys.SysPath])
import src.FixRaidenBoss2 as FRB


class RemapServiceTest(BaseFileUnitTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._path = "path/to/some/mod"
        cls._keepBackups = False
        cls._fixOnly = False
        cls._undoOnly = False
        cls._readAllInis = False
        cls._types = None
        cls._defaultType = None
        cls._log = None
        cls._verbose = False
        cls._handleExceptions = True
        cls._remapService = None

        cls._blendsCorrected = set()
        cls._blendsSkipped = {}

        cls._undoedInis = set()
        cls._removedRemapBlends = set()
        cls._removedTextures = set()

        cls._printMsgs = []

        cls._allModTypes = FRB.ModTypes.getAll()
        cls._mod: Optional[FRB.Mod] = None

    def correctBlend(self, blendStats: FRB.FileStats):
        blendStats.update(modFolder = self._mod.path, newFixed = self._blendsCorrected, newSkipped = self._blendsSkipped)
        return [self._blendsCorrected, self._blendsSkipped]
    
    def log(self, message: str):
        self._printMsgs.append(message)

    def fixIni(self, ini: FRB.IniFile):
        if (ini.file.find("bad") > -1):
            raise FloatingPointError(f"Bad ini file: {ini.file}")
        return True
    
    def removeFix(self):
        return [self._undoedInis, self._removedRemapBlends, self._removedTextures]

    def setupLog(self):
        self.patch("src.FixRaidenBoss2.Logger.log", side_effect = lambda message: self.log(message))

    def getMockLog(self) -> mock.MagicMock:
        return self.patches["src.FixRaidenBoss2.Logger.log"]
    
    def setupFixIni(self):
        self.patch("src.FixRaidenBoss2.RemapService.fixIni", side_effect = lambda ini, mod: self.fixIni(ini))

    def getMockFixIni(self) -> mock.MagicMock:
        return self.patches["src.FixRaidenBoss2.RemapService.fixIni"]
    
    def setupRemoveFix(self):
        self.patch("src.FixRaidenBoss2.Mod.removeFix", side_effect = lambda blendStats, iniStats, texStats, keepBackups, fixOnly, readAllInis: self.removeFix())

    def getMockRemoveFix(self) -> mock.MagicMock:
        return self.patches["src.FixRaidenBoss2.Mod.removeFix"]

    def setupRemapService(self):
        self._remapService = FRB.RemapService(path = self._path, keepBackups = self._keepBackups, fixOnly = self._fixOnly, undoOnly = self._undoOnly,
                                                  readAllInis = self._readAllInis, types = self._types, defaultType = self._defaultType, log = self._log,
                                                  verbose = self._verbose, handleExceptions = self._handleExceptions)
        
    def setUp(self):
        super().setUp()
        self.patch("src.FixRaidenBoss2.Mod.correctBlend", side_effect = lambda fileStats, iniPaths, fixOnly = False: self.correctBlend(fileStats))

    # ====================== path.setter =================================

    @mock.patch("src.FixRaidenBoss2.RemapService.clear")
    @mock.patch("src.FixRaidenBoss2.RemapService._setupModPath")
    def test_givenPath_pathSet(self, m_setupModPath, m_clear):
        self.setupRemapService()

        newPath = "some path/dfdfd"
        self._remapService.path = newPath
        m_clear.assert_called_once()
        self.assertEqual(m_setupModPath.call_count, 2)
        self.assertEqual(self._remapService.path, newPath)

    # ====================================================================
    # ====================== log.setter ==================================

    def test_noLogFolder_noLogPath(self):
        self.setupRemapService()

        self._remapService.log = None
        self.assertIs(self._remapService.log, None)

    def test_logFolder_setLogPath(self):
        self.setupRemapService()

        tests = {"logging": f"logging/{FRB.FileTypes.Log.value}",
                 "../../": f"../../{FRB.FileTypes.Log.value}"}

        for logPath in tests:
            self._remapService.log = logPath
            self.assertEqual(self._remapService.log, tests[logPath])

    # ====================================================================
    # ====================== clear =======================================

    def test_hasStats_allStatsCleared(self):
        self._log = "logging"
        self.setupRemapService()

        self._remapService.modStats.fixed = set([f"{i}" for i in range(60)])
        self._remapService.modStats.skipped =  {"Out, damned spot!": KeyError("out, I say!")}
        self._remapService.blendStats.fixed = {"Fair is foul and foul is fair"}
        self._remapService.blendStats.skippedByMods =  {"I am in blood": {"Stepped in so far that, should I wade no more,": KeyError("Returning were as tedious as go o'er.")}}
        self._remapService.blendStats.skipped = {"Das Wasser ist Blut... Blut...": KeyError("Blut... Blut...")}
        self._remapService.iniStats.fixed = {"Das Messer? Wo ist das Messer"}
        self._remapService.iniStats.skipped = {"Hopp, hopp! Hopp, hopp!": KeyError("Hopp, hopp!")}
        self._remapService.blendStats.removed = {"Macbeth, William Shakespeare"}
        self._remapService.blendStats.visitedAtRemoval = {"Wozzeck, Alban Berg"}
        self._remapService.iniStats.undoed = {"Beware the Jabberwock, my son!", "The jaws that bite, the claws that catch!"}
        self._remapService.logger.log("Jabberwocky, Lewis Caroll")

        self._remapService.clear(clearLog = False)

        self.compareFileStats(self._remapService.modStats, FRB.FileStats())
        self.compareFileStats(self._remapService.blendStats, FRB.FileStats())
        self.compareFileStats(self._remapService.iniStats, FRB.FileStats())
        self.compareSet(self._remapService.blendStats.visitedAtRemoval, set())
        self.assertGreater(len(self._remapService.logger.loggedTxt), 0)

        self._remapService.clear(clearLog = True)
        self.assertEqual(self._remapService.logger.loggedTxt, "")

    # ====================================================================
    # ====================== _setupModPath ===============================

    @mock.patch("src.FixRaidenBoss2.FilePathConsts.DefaultPath")
    def test_noPath_setDefaultPath(self, m_defaultPath):
        m_defaultPath.return_value = self.absPath
        self.setupRemapService()

        self._remapService._path = None
        self._remapService._setupModPath()
        self.assertEqual(self._remapService.pathIsCwd, True)
        self.assertEqual(self._remapService.path.return_value, m_defaultPath.return_value)

    def test_hasPathNotCWD_pathSetNotCWD(self):
        self.setupRemapService()

        newPath = "../The twisted path"
        self._remapService._path = newPath
        self._remapService._setupModPath()
        self.assertEqual(self._remapService.pathIsCwd, False)

        expectedPath = ntpath.normpath(self.osPathJoin(self.absPath, newPath)).replace(self.NtPathSep, self.OsSep)
        self.assertEqual(self._remapService.path, expectedPath)

    def test_pathIsCWD_pathSetAndIsCWD(self):
        self.setupRemapService()
        newPath = "."
        self._remapService._path = newPath

        with mock.patch.object(FRB.FilePathConsts, "DefaultPath", self.absPath):
            self._remapService._path = newPath
            self._remapService._setupModPath()
            self.assertEqual(self._remapService.path, self.absPath)
            self.assertEqual(self._remapService.pathIsCwd, True)

    # ====================== _setupLogPath ===============================

    def test_noLogFolder_noLogging(self):
        self.setupRemapService()

        self._remapService.log = None
        self._remapService._setupLogPath()
        self.assertIs(self._remapService.log, None)

    def test_logFolder_hasLogFilePathSet(self):
        self.setupRemapService()

        tests = {"logging": f"logging/{FRB.FileTypes.Log.value}",
                 "../../": f"../../{FRB.FileTypes.Log.value}"}

        for logPath in tests:
            self._remapService._log = logPath
            self._remapService._setupLogPath()
            self.assertEqual(self._remapService.log, tests[logPath])

    # ====================================================================
    # ====================== _setupModTypes ==============================

    def test_noModTypes_allModTypesAvailableAdded(self):
        self.setupRemapService()
        self._remapService.types = None

        self._remapService._setupModTypes("types")
        self.compareSet(self._remapService.types, self._allModTypes)

    def test_allInisRead_allModTypesAvailableAdded(self):
        self._readAllInis = True
        self.setupRemapService()
        self._remapService.types = 123

        self._remapService._setupModTypes("types")
        self.compareSet(self._remapService.types, self._allModTypes)

    def test_validModTypeSearchWords_allModTypesAvailableAdded(self):
        self.setupRemapService()
        self._remapService.types = ["raiden", "ei", "shogun"]

        self._remapService._setupModTypes("types")
        self.compareSet(self._remapService.types, {FRB.ModTypes.Raiden.value})

    def test_invalidModTypesSearchWordAllInisParsed_allModTypesAvailableAdded(self):
        self._readAllInis = True
        self.setupRemapService()
        self._remapService.types = "boo"

        self._remapService._setupModTypes("types")
        self.compareSet(self._remapService.types, self._allModTypes)

    def test_hasInvalidModTypeSearchWordNotAllInisParsed_modTypeSearchKeyWordsNotParsed(self):
        self.setupRemapService()

        self._remapService.types = ["Signora", "raiden", "ei"]
        self._remapService._setupModTypes("types")
        self.assertIsInstance(self._remapService.types, list)

        self._remapService.types = ["raiden", "ayaya", "ei"]
        self._remapService._setupModTypes("types")
        self.assertEqual(self._remapService.types, {FRB.ModTypes.Raiden.value, FRB.ModTypes.Ayaka.value})

    # ====================================================================
    # ====================== _setupDefaultModType ========================

    def test_notAllInisRead_noDefaultType(self):
        self.setupRemapService()
        self._remapService.defaultType = 123124

        self._remapService._setupDefaultModType()
        self.assertIs(self._remapService.defaultType, None)

        self._remapService.defaultType = FRB.ModTypes.Raiden.value
        self._remapService._setupDefaultModType()
        self.assertIs(self._remapService.defaultType, None)

    def test_validModTypeSearchWordReadAllInis_defaultTypeSet(self):
        self._readAllInis = True
        self.setupRemapService()
        self._remapService.defaultType = "Raiden"

        self._remapService._setupDefaultModType()
        self.assertEqual(self._remapService.defaultType, FRB.ModTypes.Raiden.value)

    def test_invalidModTypeSearchWordReadAllInis_noDefaultModType(self):
        self._readAllInis = True
        self.setupRemapService()
        self._remapService.defaultType = "Makoto"

        self._remapService._setupDefaultModType()
        self.assertEqual(self._remapService.defaultType, None)

    # ====================================================================
    # ====================== fixIni ======================================

    def test_iniNotNod_noFix(self):
        self.setupRemapService()
        ini = FRB.IniFile()
        ini.parse()
        mod = FRB.Mod(files = ["hello.txt"])

        result = self._remapService.fixIni(ini, mod)
        self.assertEqual(result, False)

    def test_iniUndoOnly_noFix(self):
        self._undoOnly = True
        self.setupRemapService()
        ini = FRB.IniFile(txt="[TextureOverrideRaidenBossBlend]\nhash=abc")
        ini.parse()
        mod = FRB.Mod(files = ["hello.txt"])

        result = self._remapService.fixIni(ini, mod)
        self.assertEqual(result, True)

    def test_iniAlreadyFixed_noFix(self):
        self.setupLog()
        self.setupRemapService()
        ini = FRB.IniFile("hello.ini")
        ini.fileTxt = "[TextureOverrideRaidenBossRemapBlend]\nhash=abc"
        ini.parse()

        mod = FRB.Mod(files = ["hello.txt"])

        result = self._remapService.fixIni(ini, mod)
        self.assertEqual(result, True)
        self.assertGreaterEqual(self.getMockLog().call_count, 2)

    @mock.patch("src.FixRaidenBoss2.IniFile.fix")
    def test_differentInisToFix_inisFixed(self, m_fix):
        self.setupLog()
        self.setupRemapService()
        ini = FRB.IniFile("hello.ini")
        ini.fileTxt = "[TextureOverrideRaidenBossBlend]\nhash=abc"
        ini.parse()

        self._mod = FRB.Mod(path = self.absPath, files = ["hello.txt"])

        tests = [[defaultdict(lambda: {}, {self.absPath: {"skippedBlend1.buf": KeyError("skippedBlend1 Error"), "skippedBlend2.buf": KeyError("skippedBlend2 Error")}}), 
                  {"fixedBlend3.buf"},
                  {"fixedBlend3.buf", "fixedBlend4.buf"}, 
                  {"skippedBlend1.buf": FloatingPointError("new skippedBlend1 Error"), "skippedBlend3.buf": FloatingPointError("skippedBlend3 Error")},
                  {"fixedBlend3.buf", "fixedBlend4.buf"}, 
                  {self.absPath: {"skippedBlend1.buf": FloatingPointError("new skippedBlend1 Error"), "skippedBlend2.buf": KeyError("skippedBlend2 Error"),  "skippedBlend3.buf": FloatingPointError("skippedBlend3 Error")}}]]
        
        for test in tests:
            self._remapService.clear()
            self._remapService.blendStats.skippedByMods = test[0]
            self._remapService.blendStats.fixed = test[1]
            self._blendsCorrected = test[2]
            self._blendsSkipped = test[3]

            result = self._remapService.fixIni(ini, self._mod)
            self.assertEqual(result, True)
            self.compareSet(self._remapService.blendStats.fixed, test[4])
            
            expectedSkippedBlendsByMods = test[5]
            self.assertEqual(len(expectedSkippedBlendsByMods), len(self._remapService.blendStats.skippedByMods))
            for modPath in expectedSkippedBlendsByMods:
                self.assertIn(modPath, self._remapService.blendStats.skippedByMods)

                expectedModBlendErrors = expectedSkippedBlendsByMods[modPath]
                resultModBlendErrors = self._remapService.blendStats.skippedByMods[modPath]

                self.assertEqual(len(expectedModBlendErrors), len(resultModBlendErrors))
                for blendPath in expectedModBlendErrors:
                    self.assertIn(blendPath, resultModBlendErrors)
                    self.assertEqual(type(expectedModBlendErrors[blendPath]), type(resultModBlendErrors[blendPath]))

    # ====================================================================
    # ====================== fixMod ======================================

    @mock.patch("src.FixRaidenBoss2.Mod.removeBackupInis")
    @mock.patch("src.FixRaidenBoss2.IniFile.checkIsMod", side_effect = lambda: True)
    def test_differentMods_modsFixed(self, m_checkIsMod, m_removeBackupInis):
        self.setupLog()
        self.setupFixIni()
        self.setupRemoveFix()
        self.setupRemapService()
        getAbsPath = lambda file: self.osPathJoin(self.absPath, file)

        tests = [[FRB.Mod(path = self.absPath, files = []), [], {"fixedIni1", "fixedIni2"}, {getAbsPath("skippedIni1"): KeyError("Ini1 skipped"), getAbsPath("skippedIni2"): KeyError("Ini2 skipped")}, 
                  {"skippedMod1": KeyError("mod1 skipped")}, {"removedRemap1"}, {"removedRemap2", "removedRemap3"},
                  False, {"fixedIni1", "fixedIni2"}, {getAbsPath("skippedIni1"): KeyError("Ini1 skipped"), getAbsPath("skippedIni2"): KeyError("Ini2 skipped")}, {"skippedMod1": KeyError("mod1 skipped")},
                  {"removedRemap1", "removedRemap2", "removedRemap3"}],

                 [FRB.Mod(path = self.absPath, files = []), [FRB.IniFile("modIni1")], {"fixedIni1", "fixedIni2"}, {getAbsPath("skippedIni1"): KeyError("Ini1 skipped"), getAbsPath("skippedIni2"): KeyError("Ini2 skipped")}, 
                  {"skippedMod1": KeyError("mod1 skipped")}, {"removedRemap1"}, {"removedRemap2", "removedRemap3"},
                  True, {"fixedIni1", "fixedIni2", f"{self.absPath}/modIni1"}, {getAbsPath("skippedIni1"): KeyError("Ini1 skipped"), getAbsPath("skippedIni2"): KeyError("Ini2 skipped")}, {"skippedMod1": KeyError("mod1 skipped")},
                  {"removedRemap1", "removedRemap2", "removedRemap3"}],
                  
                 [FRB.Mod(path = self.absPath, files = []), [FRB.IniFile("modIni1"), FRB.IniFile("bad_modIni2"), FRB.IniFile("modIni3")], set(), {}, {}, set(), set(),
                  True, {f"{self.absPath}/modIni1", f"{self.absPath}/modIni3"}, {getAbsPath("bad_modIni2"): FloatingPointError(f"Bad ini file: bad_modIni2")},
                  {}, set()],

                 [FRB.Mod(path = self.absPath, files = []), [FRB.IniFile("bad_modIni1"), FRB.IniFile("bad_modIni2"), FRB.IniFile("bad_modIni3")], set(), {}, {}, set(), set(),
                  False, set(), {getAbsPath("bad_modIni1"): FloatingPointError(f"Bad ini file: bad_modIni1"), 
                              getAbsPath("bad_modIni2"): FloatingPointError(f"Bad ini file: bad_modIni2"), 
                              getAbsPath("bad_modIni3"): FloatingPointError(f"Bad ini file: bad_modIni3")}, {self.absPath: FloatingPointError(f"Bad ini file: bad_modIni1")}, set()]]


        checkIsModTotalCallCount = 0
        for test in tests:
            self._remapService.clear()
            self._remapService.iniStats.fixed = test[2]
            self._remapService.iniStats.skipped = test[3]
            self._remapService.modStats.skipped = test[4]
            self._remapService.blendStats.updateRemoved(test[5])
            self._removedRemapBlends = test[6]

            self._mod = test[0]
            self._mod.inis = {}
            for ini in test[1]:
                self._mod.inis[ini.file] = ini

            result = self._remapService.fixMod(self._mod)
            self.assertEqual(result, test[7])
            self.compareSet(self._remapService.iniStats.fixed, test[8])
            self.compareSet(self._remapService.blendStats.removed, test[11])

            checkIsModTotalCallCount += len(self._mod.inis)
            self.assertEqual(m_checkIsMod.call_count, checkIsModTotalCallCount)

            expectedSkippedInis = test[9]
            resultSkippedInis = self._remapService.iniStats.skipped
            self.assertEqual(len(resultSkippedInis), len(expectedSkippedInis))
            for ini in expectedSkippedInis:
                self.assertIn(ini, resultSkippedInis)
                self.assertEqual(type(resultSkippedInis[ini]), type(expectedSkippedInis[ini]))

            expectedSkippedMods = test[10]
            resultSkippedMods = self._remapService.modStats.skipped
            self.assertEqual(len(resultSkippedMods), len(expectedSkippedMods))
            for skippedMod in expectedSkippedMods:
                self.assertIn(skippedMod, resultSkippedMods)
                self.assertEqual(type(resultSkippedMods[skippedMod]), type(expectedSkippedMods[skippedMod]))

    # ====================================================================