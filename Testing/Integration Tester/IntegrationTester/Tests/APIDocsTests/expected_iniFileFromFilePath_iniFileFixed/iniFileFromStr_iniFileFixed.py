import sys
import os

from IntegrationTester.src.constants.ConfigKeys import ConfigKeys
from IntegrationTester.src.Config import Config

sys.path.insert(1, Config[ConfigKeys.SysPath])
import src.FixRaidenBoss2 as FRB


shortWackyRaidenIniTxt = r"""
[Constants]
global persist $swapvar = 0
global persist $swapvarn = 0
global persist $swapmain = 0
global persist $swapoffice = 0
global persist $swapglasses = 0

[KeyVar]
condition = $active == 1
key = VK_DOWN
type = cycle
$swapvar = 0,1,2

[KeyIntoTheHole]
condition = $active == 1
key = VK_RIGHT
type = cycle
$swapvarn = 0,1

; The top part is not really important, so I not going to finish
;   typing all the key swaps... 😋
;
; The bottom part is what the fix actually cares about

[TextureOverrideRaidenShogunBlend]
run = CommandListRaidenShogunBlend
handling = skip
draw = 21916,0

[CommandListRaidenShogunBlend]
if $swapmain == 0
    if $swapvar == 0 && $swapvarn == 0
        vb1 = ResourceRaidenShogunBlend.0
    else
        vb1 = ResourceEiBlendsHerBlenderInsteadOfHerSmoothie
    endif
else if $swapmain == 1
    run = SubSubTextureOverride
endif

[SubSubTextureOverride]
if $swapoffice == 0 && $swapglasses == 0
    vb1 = GIMINeedsResourcesToAllStartWithResource
endif

[ResourceRaidenShogunBlend.0]
type = Buffer
stride = 32
filename = ..\..\..\../../../../../../2-BunnyRaidenShogun\RaidenShogunBlend.buf

[ResourceEiBlendsHerBlenderInsteadOfHerSmoothie]
type = Buffer
stride = 32
if $swapmain == 1
    filename = M:\AnotherDrive\CuteLittleEi.buf
else
    run = RaidenPuppetCommandResource
endif

[GIMINeedsResourcesToAllStartWithResource]
type = Buffer
stride = 32
filename = ./../AAA/BBBB\CCCCCC\DDDDDRemapBlend.buf

[RaidenPuppetCommandResource]
type = Buffer
stride = 32
filename = ./Dont/Use\If/Statements\Or/SubCommands\In/Resource\Sections.buf
"""


iniFile = FRB.IniFile(txt = shortWackyRaidenIniTxt, modTypes = FRB.ModTypes.getAll())
iniFile.parse()
fixedResult = iniFile.fix()

iniPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CuteLittleRaiden.ini")
with open(iniPath, "w", encoding = "utf-8") as f:
    f.write(fixedResult)