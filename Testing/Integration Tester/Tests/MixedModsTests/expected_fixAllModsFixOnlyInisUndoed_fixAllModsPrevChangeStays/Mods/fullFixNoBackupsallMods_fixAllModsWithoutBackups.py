import sys
import os

sys.path.insert(1, '../../Fix-Raiden-Boss 2.0 (for all user )')
import src.FixRaidenBoss2.FixRaidenBoss2 as FRB


iniRunPath = FRB.FileService.parseOSPath(os.path.dirname(os.path.abspath(__file__)))
logPath = FRB.FileService.parseOSPath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Logs"))

fixService = FRB.BossFixService(path = iniRunPath, verbose = False, keepBackups = False, log = logPath, readAllInis = True)
fixService.fix()