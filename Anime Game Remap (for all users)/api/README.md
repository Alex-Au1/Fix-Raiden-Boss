# Anime Game Remap (AG Remap)
#### *Previously Known as <ins>FixRaidenBoss2</ins>*
[![PyPI](https://img.shields.io/pypi/pyversions/FixRaidenBoss2)](https://www.python.org/downloads/)
[![PyPI - Version](https://img.shields.io/pypi/v/FixRaidenBoss2?label=FixRaidenBoss2%20pypi)](https://pypi.org/project/FixRaidenBoss2/)
[![PyPI - Version](https://img.shields.io/pypi/v/AnimeGameRemap?label=AG%20Remap%20pypi)](https://pypi.org/project/AnimeGameRemap/)
[![Documentation Status](https://readthedocs.org/projects/anime-game-remap/badge/?version=latest)](https://anime-game-remap.readthedocs.io/en/latest/?badge=latest)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nhok0169/Anime-Game-Remap/unit-tests.yml?label=Unit%20Tests)](https://github.com/nhok0169/Anime-Game-Remap/actions/workflows/unit-tests.yml)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nhok0169/Anime-Game-Remap/integration-tests.yml?label=Integration%20Tests)](https://github.com/nhok0169/Anime-Game-Remap/actions/workflows/integration-tests.yml)

[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/nhok0169/Anime-Game-Remap/total?label=Github%20Downloads)](https://github.com/nhok0169/Anime-Game-Remap/releases/latest)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/FixRaidenBoss2?label=FixRaidenBoss2%20Pypi%20Downloads)](https://pypi.org/project/FixRaidenBoss2/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/AnimeGameRemap?label=AG%20Remap%20Pypi%20Downloads)](https://pypi.org/project/AnimeGameRemap)


<a href="https://github.com/nhok0169/Anime-Game-Remap/tree/nhok0169/Anime%20Game%20Remap%20(for%20all%20users)/api"><img alt="" src="https://github.com/nhok0169/Anime-Game-Remap/raw/nhok0169/Docs/src/_static/images/raiden.jpg" style="width:750px; height: auto;"></a>
- Author Ideal [NK#1321](https://discordapp.com/users/277117247523389450)
- Thank [SilentNightSound#7430](https://github.com/SilentNightSound) for the logic rewrite
- Thank HazrateGolabi#1364 for combine and make final script
- Thank [Albert Gold#2696](https://github.com/Alex-Au1) for update the code for merged mods
## Requirements 
- [Python (version 3.6 and up)](https://www.python.org/downloads/)

<br>

> [!WARNING]  
> Remapping mods is overall a hacky process. Please see a mod's [remap grading](https://anime-game-remap.readthedocs.io/en/latest/remapGrading.html) for the current limitations
> of remapping a particular mod before posting an issue

<br>

## VIDEO TUTORIAL AND EXAMPLES:

### Quickstart
**Individual Mod:** https://www.youtube.com/watch?v=29FM0GywcWA  
**Merged Mods:** https://www.youtube.com/watch?v=nEyMYIHdrQM  
**Mega Merged Mods:** https://www.youtube.com/watch?v=08co5ct7zeg  

### More Features
[More examples here](https://github.com/nhok0169/Anime-Game-Remap/tree/nhok0169/Examples)

<br>

## How to Run
- Choose your pick of which way to run the script:

  - **Choice A:** &nbsp; [Quickstart!](#choice-a-lets-start--) 🟢 &nbsp;&nbsp; (for beginners)
  - **Choice B:** &nbsp; [CMD WITHOUT a Script](#choice-b-run-on-cmd-without-a-script-) 🟡 &nbsp;&nbsp; (recommended if you run by CMD)
  - **Choice C:** &nbsp; [CMD with a Script](#choice-c-run-on-cmd-with-a-script-) 🟡 &nbsp;&nbsp; (the convention that other GIMI scripts follow)
  - **Choice D:** &nbsp; [API](#choice-d-api-usage-)  🟠 &nbsp;&nbsp; (for expert coders)

<br>

## Choice A: Let's Start ! 🟢
### STEP 1:
- Go to the [Latest Release](https://github.com/nhok0169/Anime-Game-Remap/releases/latest) and click on the ``FixRaidenBoss2.py`` link to download the script into your Mod's folder or GIMI's `Mod` folder.

*Make sure the `.ini` files contain the section named `[TextureOverrideRaidenShogunBlend]` or use the `--all` option to read all .ini files the program encounters*
### STEP 2:
- Double click on the script
### STEP 3:
- Open the game and enjoy it

## Choice B: Run on CMD Without a Script 🟡
### STEP 1:
- Install the module onto your computer by [opening cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd) and typing :
```python
python -m pip install -U FixRaidenBoss2
```
then enter

*( you can now run the program anywhere without copying a script! )*

### STEP 2:
- [open cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd) in your Raiden Mod folder or GIMI's `Mod` folder and type:
```python
python -m FixRaidenBoss2
```
then enter

*Make sure the `.ini` files contain the section named `[TextureOverrideRaidenShogunBlend]` or use the `--all` option to read all .ini files the program encounters*
### STEP 3:
- Open the game and enjoy it

## Choice C: Run on CMD With a Script 🟡
### STEP 1:
- Go to the [Latest Release](https://github.com/nhok0169/Anime-Game-Remap/releases/latest) and click on the ``FixRaidenBoss2.py`` link to download the script into your Raiden Mod folder or GIMI's `Mod` folder.

### STEP 2:
- [open cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd) and type
```python
python FixRaidenBoss2.py
```
then enter

*Make sure the `.ini` files contain the section named `[TextureOverrideRaidenShogunBlend]` or use the `--all` option to read all .ini files the program encounters*
### STEP 3:
- Open the game and enjoy it

## Command Options
| Options | Description |
| --- | --- |
| -h, --help | show this help message and exit |
| -s str, --src str | The starting path to run this fix. If this option is not specified, then will run the fix from the current directory. |
| -v str, --version str | The game version we want the fix to be compatible with. If this option is not specified, then will use the latest game version. |
| -d, --deleteBackup | deletes backup copies of the original .ini files |
| -f, --fixOnly | only fixes the mod without cleaning any previous runs of the script |
| -u, --undo | Undo the previous runs of the script |
| -l str, --log str | The folder location to log the printed out text into a seperate .txt file. If this option is not specified, then will not log the printed out text. |
| -a, --all | Parses all *.ini files that the program encounters. This option supersedes the --types |
| -dt str, --defaultType str | The default mod type to use if the *.ini file belongs to some unknown mod <br> If the --all option is set to True, then this argument will be 'raiden'. <br> Otherwise, if this value is not specified, then any mods with unknown types will be skipped <br> <br> See below for the different names/aliases of the supported types of mods. |
| -t str, --types str | Parses *.ini files that the program encounters for only specific types of mods. If the --all option has been specified, this option has no effect. <br> By default, if this option is not specified, will parse the *.ini files for all the supported types of mods. <br> <br> Please specify the types of mods using the the mod type's name or alias, then seperate each name/alias with a comma(,) <br> &nbsp; &nbsp; &nbsp; *eg. raiden,arlecchino,ayaya* |
| -rt str, --remappedTypes str |  From all the mods to fix, specified by the --types option, will specifically remap those mods to the mods specified by this option. <br> For a mod specified by the --types option, if none of its corresponding remapped mods are specified by this option, then the mod specified by the --types option will be remapped to all its corresponding mods. <br> <br> ------------------- <br> eg. <br> If this program was ran with the following options: <br> --types kequeen,jean <br> --remappedTypes jeanSea <br> <br> the program will do the following remap: <br> keqing --> keqingOpulent <br> Jean --> JeanSea <br> <br> Note that Jean will not remap to JeanCN <br> ------------------- <br> <br> By default, if this option is not specified, will remap all the mods specified in --types to their corresponding remapped mods. <br> <br> Please specify the types of mods using the the mod type's name or alias, then seperate each name/alias with a comma(,) <br> eg. raiden,arlecchino,ayaya <br> <br> See below for the different names/aliases of the supported types of mods. |

<br>

## Mod Types
Below are the supported types of mods

| Name | Aliases | Description |
| --- | --- | ---|
| Amber | BaronBunny, ColleisBestie | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Amber)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| AmberCN | BaronBunnyCN, ColleisBestieCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(AmberCN)((?!RemapBlend).)*Blend.*\s*\]` |
| Arlecchino | Father, Harlequin, Knave, Perrie, Peruere | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Arlecchino)((?!RemapBlend).)*Blend.*\s*\]` |
| Barbara | Healer, Idol | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Barbara)((?!RemapBlend|Summertime).)*Blend.*\s*\]` |
| BarabaraSummertime | BarbaraBikini, HealerSummertime, IdolSummertime | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(BarbaraSummertime)((?!RemapBlend).)*Blend.*\s*\]` |
| Ganyu | Cocogoat | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Ganyu)((?!(RemapBlend|Twilight)).)*Blend.*\s*\]` |
| GanyuTwilight | CocogoatLanternRite, CocogoatTwilight, GanyuLanternRite, LanternRiteCocogoat, LanternRiteGanyu | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(GanyuTwilight)((?!(RemapBlend)).)*Blend.*\s*\]` |
| Jean | ActingGrandMaster, KleesBabySitter | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Jean)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| JeanCN | ActingGrandMasterCN, KleesBabySitterCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(JeanCN)((?!RemapBlend).)*Blend.*\s*\]` |
| JeanSea | ActingGrandMasterSea, KleesBabySitterSea | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(JeanSea)((?!RemapBlend|CN).)*Blend.*\s*\]` |
| Keqing | Kequeen, MoraxSimp, ZhongliSimp | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Keqing)((?!(RemapBlend|Opulent)).)*Blend.*\s*\]` |
| KeqingOpulent | CuterKeqing, CuterKequeen, KeqingLaternRite, KequeenLanternRite, KequeenOpulent, LanternRiteKeqing, LanternRiteKequeen, LaternRiteMoraxSimp, LaternRiteZhongliSimp, MoraxSimpLaternRite, MoraxSimpOpulent, ZhongliSimpLaternRite, ZhongliSimpOpulent | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(KeqingOpulent)((?!RemapBlend).)*Blend.*\s*\]` |
| Mona | BigHat, NoMora | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Mona)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| MonaCN | BigHatCN, NoMoraCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(MonaCN)((?!RemapBlend).)*Blend.*\s*\]` |
| Ningguang | GeoMommy, SugarMommy | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Ningguang)((?!(RemapBlend|Orchid)).)*Blend.*\s*\]` |
| NingguangOrchid | GeoMommyLaternRite, GeoMommyOrchid, LanternRiteNingguang, LanternRiteSugarMommy, LaternRiteGeoMommy, NingguangLanternRite, SugarMommyLanternRite, SugarMommyOrchid | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(NingguangOrchid)((?!RemapBlend).)*Blend.*\s*\]` |
| Raiden | Cryden, CrydenShogun, Ei, RaidenEi, RaidenShogun, RaidenShotgun, Shogun, Shotgun, SmolEi | check if the .ini file contains a section matching the regex, `^\s\*\[\s\*TextureOverride.\*(Raiden\|Shogun)((?!RemapBlend).)\*Blend.\*\s\*\]` |
| Rosaria | GothGirl | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Rosaria)((?!(RemapBlend|CN)).)*Blend.*\s*\]` |
| RosariaCN | GothGirlCN | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(RosariaCN)((?!RemapBlend).)*Blend.*\s*\]` |
| Shenhe | RedRopes, YelansBestie | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(Shenhe)((?!RemapBlend|FrostFlower).)*Blend.*\s*\]` |
| ShenheFrostFlower | LanternRiteRedRopes, LanternRiteShenhe, LanternRiteYelansBestie, RedRopesFrostFlower, RedRopesLanternRite, ShenheLanternRite, YelansBestieFrostFlower, YelansBestieLanternRite | check if the .ini file contains a section matching the regex, `^\s*\[\s*TextureOverride.*(ShenheFrostFlower)((?!RemapBlend).)*Blend.*\s*\]` |
<br>
<br>

## Choice D: API Usage 🟠

Tool developpers can now include the fix within their code!

### API Documentation
For more info about how to use the API, visit the documentation at https://anime-game-remap.readthedocs.io/en/latest/

<br>

### API Setup

<br>

*Make sure you first install the module by typing into [cmd](https://www.google.com/search?q=how+to+open+cmd+in+a+folder&oq=how+to+open+cmd):*
```bash
python -m pip install -U FixRaidenBoss2
```
<br>

### API Examples

See the documentation for more detailed [examples](https://anime-game-remap.readthedocs.io/en/latest/apiExamples.html) on how to use the API.

<br>

Below is a ***preview*** that gives a feel of using the API

<br>

*eg. Running the following code under [this folder](https://github.com/nhok0169/Anime-Game-Remap/tree/nhok0169/Testing/Integration%20Tester/IntegrationTester/Tests/MixedModsTests/inputs/Mods)*

```python
import FixRaidenBoss2 as FRB

fixService = FRB.RemapService(keepBackups = False)
fixService.fix()

print("The Raiden Mod is fixed!")
```
<br>

<details>
<summary>Example Result</summary>
<br>

```
===== Types of Mods To Fix =====

- Amber
- AmberCN
- Arlecchino
- Barbara
- BarbaraSummertime
- Ganyu
- GanyuTwilight
- Jean
- JeanCN
- JeanSea
- Keqing
- KeqingOpulent
- Mona
- MonaCN
- Ningguang
- NingguangOrchid
- Raiden
- Rosaria
- RosariaCN
- Shenhe
- ShenheFrostFlower

================================


# Mods\Arlecchino -->
# Mods\Arlecchino --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods\Arlecchino -->
# Mods\Arlecchino --> KeyError: "The section by the name 'glitchedOutResource' does not exist"
# Mods\Arlecchino -->
# Mods\Arlecchino --> Traceback (most recent call last):
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\IniSectionGraph.py", line 248, in getSection
# Mods\Arlecchino -->     ifTemplate = self._allSections[sectionName]
# Mods\Arlecchino --> KeyError: 'glitchedOutResource'
# Mods\Arlecchino -->
# Mods\Arlecchino --> The above exception was the direct cause of the following exception:
# Mods\Arlecchino -->
# Mods\Arlecchino --> Traceback (most recent call last):
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\Mod.py", line 425, in removeFix
# Mods\Arlecchino -->     ini.parse()
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\IniFile.py", line 2264, in parse
# Mods\Arlecchino -->     parser.parse()
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\strategies\iniParsers\GIMIParser.py", line 176, in parse
# Mods\Arlecchino -->     self.resourceCommandsGraph.build(newTargetSections = resourceCommandLst, newAllSections = self._iniFile.sectionIfTemplates)
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\IniSectionGraph.py", line 218, in build
# Mods\Arlecchino -->     self.construct()
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\IniSectionGraph.py", line 307, in construct
# Mods\Arlecchino -->     ifTemplate = self.getSection(sectionName)
# Mods\Arlecchino -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\IniSectionGraph.py", line 251, in getSection
# Mods\Arlecchino -->     raise KeyError(f"The section by the name '{sectionName}' does not exist") from e
# Mods\Arlecchino --> KeyError: "The section by the name 'glitchedOutResource' does not exist"
# Mods\Arlecchino -->
# Mods\Arlecchino --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods\Arlecchino -->
# Mods\Arlecchino --> Removing any previous changes from this script in good_merged.ini
# Mods\Arlecchino -->
# Mods\Arlecchino --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\Arlecchino1\ArlecchinoBossRemapBlend.buf
# Mods\Arlecchino --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\Arlecchino2\ArlecchinoBossRemapBlend.buf
# Mods\Arlecchino -->
# Mods\Arlecchino --> the ini file, bad_merged.ini, has alreaedy encountered an error
# Mods\Arlecchino --> Parsing good_merged.ini...
# Mods\Arlecchino --> Fixing the Blend.buf files for good_merged.ini...
# Mods\Arlecchino --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\Arlecchino1\ArlecchinoBossRemapBlend.buf
# Mods\Arlecchino --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\Arlecchino2\ArlecchinoBossRemapBlend.buf
# Mods\Arlecchino --> Making the fixed ini file for good_merged.ini
# Mods\Arlecchino -->

# Mods\Arlecchino\Arlecchino1 --> Removing any previous changes from this script in DISABLED_arlecchino.ini
# Mods\Arlecchino\Arlecchino1 -->
# Mods\Arlecchino\Arlecchino1 --> Parsing DISABLED_arlecchino.ini...
# Mods\Arlecchino\Arlecchino1 --> Fixing the Blend.buf files for DISABLED_arlecchino.ini...
# Mods\Arlecchino\Arlecchino1 --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\Arlecchino1\ArlecchinoBossRemapBlend.buf
# Mods\Arlecchino\Arlecchino1 --> Making the fixed ini file for DISABLED_arlecchino.ini
# Mods\Arlecchino\Arlecchino1 -->

# Mods\Arlecchino\Arlecchino2 --> Removing any previous changes from this script in DISABLED_arlecchino.ini
# Mods\Arlecchino\Arlecchino2 -->
# Mods\Arlecchino\Arlecchino2 --> Parsing DISABLED_arlecchino.ini...
# Mods\Arlecchino\Arlecchino2 --> Fixing the Blend.buf files for DISABLED_arlecchino.ini...
# Mods\Arlecchino\Arlecchino2 --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\Arlecchino2\ArlecchinoBossRemapBlend.buf
# Mods\Arlecchino\Arlecchino2 --> Making the fixed ini file for DISABLED_arlecchino.ini
# Mods\Arlecchino\Arlecchino2 -->

# Mods\Arlecchino\Ugly --> Removing any previous changes from this script in shawshank redemption.ini
# Mods\Arlecchino\Ugly -->
# Mods\Arlecchino\Ugly --> Parsing shawshank redemption.ini...
# Mods\Arlecchino\Ugly --> Fixing the Blend.buf files for shawshank redemption.ini...
# Mods\Arlecchino\Ugly --> Making the fixed ini file for shawshank redemption.ini
# Mods\Arlecchino\Ugly -->

# Mods\Ayaka\Arlecchino --> Removing any previous changes from this script in arlecchino.ini
# Mods\Ayaka\Arlecchino -->
# Mods\Ayaka\Arlecchino --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ayaka\Arlecchino\arlecchinoArlecchinoBossRemapBlend.buf
# Mods\Ayaka\Arlecchino -->
# Mods\Ayaka\Arlecchino --> Parsing arlecchino.ini...
# Mods\Ayaka\Arlecchino --> Fixing the Blend.buf files for arlecchino.ini...
# Mods\Ayaka\Arlecchino --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ayaka\Arlecchino\arlecchinoArlecchinoBossRemapBlend.buf
# Mods\Ayaka\Arlecchino --> Making the fixed ini file for arlecchino.ini
# Mods\Ayaka\Arlecchino -->

# Mods\Ayaka\Raiden --> Removing any previous changes from this script in raiden.ini
# Mods\Ayaka\Raiden -->
# Mods\Ayaka\Raiden --> Parsing raiden.ini...
# Mods\Ayaka\Raiden --> Fixing the Blend.buf files for raiden.ini...
# Mods\Ayaka\Raiden --> Making the fixed ini file for raiden.ini
# Mods\Ayaka\Raiden -->

# Mods\Ei\Raiden --> Removing any previous changes from this script in tri_merge_core.ini
# Mods\Ei\Raiden -->
# Mods\Ei\Raiden --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\BodyEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\LeftWingEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\RightWingEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden -->
# Mods\Ei\Raiden --> Parsing tri_merge_core.ini...
# Mods\Ei\Raiden --> Fixing the Blend.buf files for tri_merge_core.ini...
# Mods\Ei\Raiden --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\BodyEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\LeftWingEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\RightWingEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden --> Making the fixed ini file for tri_merge_core.ini
# Mods\Ei\Raiden -->

# Mods\Ei\Raiden\leftWing --> Removing any previous changes from this script in left_wing_merge.ini
# Mods\Ei\Raiden\leftWing -->
# Mods\Ei\Raiden\leftWing --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\listeners\heartListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\controllers\heartPumpControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\listeners\rightWingListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\controllers\rightWingControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing -->
# Mods\Ei\Raiden\leftWing --> Parsing left_wing_merge.ini...
# Mods\Ei\Raiden\leftWing --> Fixing the Blend.buf files for left_wing_merge.ini...
# Mods\Ei\Raiden\leftWing --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\listeners\heartListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\controllers\heartPumpControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\LeftWingEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\listeners\rightWingListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\controllers\rightWingControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\leftWing --> Making the fixed ini file for left_wing_merge.ini
# Mods\Ei\Raiden\leftWing -->

# Mods\Ei\Raiden\rightWing --> Removing any previous changes from this script in right_wing_merge.ini
# Mods\Ei\Raiden\rightWing -->
# Mods\Ei\Raiden\rightWing --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\listeners\leftWingListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\controllers\leftWingControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing -->
# Mods\Ei\Raiden\rightWing --> Parsing right_wing_merge.ini...
# Mods\Ei\Raiden\rightWing --> Fixing the Blend.buf files for right_wing_merge.ini...
# Mods\Ei\Raiden\rightWing --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\listeners\heartListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\controllers\heartPumpControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\listeners\leftWingListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\controllers\leftWingControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\RightWingEntityRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\rightWing --> Making the fixed ini file for right_wing_merge.ini
# Mods\Ei\Raiden\rightWing -->

# Mods\Ei\Raiden\Body\Center --> Removing any previous changes from this script in heart.ini
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\Body\whoopsIReferencedTheWrongThingRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center --> No Previous RemapBlend.buf found at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Makoto\MakotoRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> Parsing heart.ini...
# Mods\Ei\Raiden\Body\Center --> Fixing the Blend.buf files for heart.ini...
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> FileNotFoundError: [Errno 2] No such file or directory: 'Anime-Game-Remap\\Testing\\Integration Tester\\IntegrationTester\\Tests\\MixedModsTests\\inputs\\Mods\\Ei\\Raiden\\Body\\whoopsIReferencedTheWrongThing.buf'
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> Traceback (most recent call last):
# Mods\Ei\Raiden\Body\Center -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\Mod.py", line 604, in correctBlend
# Mods\Ei\Raiden\Body\Center -->     correctedBlendPath = self.blendCorrection(origFullPath, modType, modName, fixedBlendFile = fixedFullPath, version = self.version)
# Mods\Ei\Raiden\Body\Center -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\Mod.py", line 519, in blendCorrection
# Mods\Ei\Raiden\Body\Center -->     blend = BlendFile(blendFile)
# Mods\Ei\Raiden\Body\Center -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\BlendFile.py", line 63, in __init__
# Mods\Ei\Raiden\Body\Center -->     self._data = self.read()
# Mods\Ei\Raiden\Body\Center -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\BlendFile.py", line 75, in read
# Mods\Ei\Raiden\Body\Center -->     return self.readFile(self.src)
# Mods\Ei\Raiden\Body\Center -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\model\BlendFile.py", line 79, in readFile
# Mods\Ei\Raiden\Body\Center -->     result = FileService.readBinary(blendSrc)
# Mods\Ei\Raiden\Body\Center -->   File "path\to\windows\computer\user\AppData\Local\Programs\Python\Python39\lib\site-packages\FixRaidenBoss2\tools\files\FileService.py", line 511, in readBinary
# Mods\Ei\Raiden\Body\Center -->     with open(src, "rb") as f:
# Mods\Ei\Raiden\Body\Center --> FileNotFoundError: [Errno 2] No such file or directory: 'Anime-Game-Remap\\Testing\\Integration Tester\\IntegrationTester\\Tests\\MixedModsTests\\inputs\\Mods\\Ei\\Raiden\\Body\\whoopsIReferencedTheWrongThing.buf'
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods\Ei\Raiden\Body\Center -->
# Mods\Ei\Raiden\Body\Center --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\listeners\leftWingListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\leftWing\controllers\leftWingControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center --> Blend file correction done at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Makoto\MakotoRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\listeners\rightWingListenerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center --> Blend file has already been corrected at Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Ei\Raiden\rightWing\controllers\rightWingControllerRaidenBossRemapBlend.buf
# Mods\Ei\Raiden\Body\Center --> Making the fixed ini file for heart.ini
# Mods\Ei\Raiden\Body\Center -->

# Mods -->
# Mods --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods -->
# Mods --> WARNING: The following *.ini files were skipped due to warnings (see log above):
# Mods -->
# Mods --> - Anime-Game-Remap\Testing\Integration Tester\IntegrationTester\Tests\MixedModsTests\inputs\Mods\Arlecchino\bad_merged.ini:
# Mods -->      --- KeyError ---
# Mods -->      "The section by the name 'glitchedOutResource' does not exist"
# Mods -->
# Mods -->
# Mods --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods -->
# Mods -->
# Mods -->
# Mods --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods -->
# Mods --> WARNING: The following Blend.buf files were skipped due to warnings (see log above):
# Mods -->
# Mods --> ===== Mod: Mods\Ei\Raiden\Body\Center =====
# Mods -->
# Mods --> - Ei\Raiden\Body\whoopsIReferencedTheWrongThingRaidenBossRemapBlend.buf:
# Mods -->      --- FileNotFoundError ---
# Mods -->      [Errno 2] No such file or directory: 'Anime-Game-Remap\\Testing\\Integration Tester\\IntegrationTester\\Tests\\MixedModsTests\\inputs\\Mods\\Ei\\Raiden\\Body\\whoopsIReferencedTheWrongThing.buf'
# Mods -->
# Mods --> ===========================================
# Mods -->
# Mods --> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Mods -->
# Mods -->
# Mods -->
# Mods --> ========== Summary ==========
# Mods -->
# Mods --> - Out of 10 found mods, fixed 10 mods and skipped 0 mods
# Mods --> - Out of the 11 *.ini files within the found mods, fixed 10 *.ini files and skipped 1 *.ini files
# Mods --> - Out of the 14 Blend.buf files within the found mods, fixed 13 Blend.buf files and skipped 1 Blend.buf files
# Mods --> - Removed fix from up to 10 *.ini files
# Mods -->
# Mods --> =============================
# Mods -->
```
</details>
<br>