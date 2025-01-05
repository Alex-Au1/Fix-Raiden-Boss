
#
# ===== Note =====
#
# This library was auto-generated by AG Remap's APIMirrorBuilder tool,
#   a build system tool used in AG Remap's CI pipeline that creates a mirror for the existing
#   API source code since we cannot rename the original name of 'FixRaidenBoss2' to 'Anime Game Remap' in Pypi,
#   therefore, we decided to make a brand new package that mirrors the original API.
#
# ***** APIMirrorBuilder Stats *****
#
# Version: 1.0.0
# Authors: Albert Gold#2696
# Datetime Ran: Sunday, January 05, 2025 04:10:39.995 PM UTC
# Run Hash: 67c51d06-d847-4eb5-a2ab-fd3fe5246361
# 
# **********************************
# ================
#

# ===== Anime Game Remap (AG Remap) =====
# Authors: NK#1321, Albert Gold#2696
#
# if you used it to remap your mods pls give credit for "Nhok0169" and "Albert Gold#2696"
# Special Thanks:
#   nguen#2011 (for support)
#   SilentNightSound#7430 (for internal knowdege so wrote the blendCorrection code)
#   HazrateGolabi#1364 (for being awesome, and improving the code)

#
# ***** AG Remap Stats *****
#
# Version: 4.2.1
# Authors: Albert Gold#2696, NK#1321
# Datetime Compiled: Sunday, January 05, 2025 04:10:39.995 PM UTC
# Build Hash: 685f3a84-4e7a-4f66-a53b-8037eaf4c9f7
#
# **************************
#

from FixRaidenBoss2 import Colours, ColourConsts, FileExt, FileTypes, FileEncodings, FilePrefixes, FileSuffixes, FilePathConsts, ImgFormats, IniKeywords, IniBoilerPlate, GIBuilder, IfPredPartType, ModTypeBuilder, ModTypes, TexMetadataNames, ShortCommandOpts, CommandOpts, HashData, IndexData, VGRemapData, BadBlendData, BlendFileNotRecognized, ConflictingOptions, DuplicateFileException, Error, FileException, InvalidModType, MissingFileException, NoModType, RemapMissingBlendFile, Hashes, Indices, ModAssets, ModIdAssets, VGRemaps, BlendFile, File, IniFile, TextureFile, KeepFirstDict, BaseIniFixer, GIMIFixer, GIMIObjMergeFixer, GIMIObjRegEditFixer, GIMIObjReplaceFixer, GIMIObjSplitFixer, IniFixBuilder, MultiModFixer, BaseRegEditFilter, RegEditFilter, RegNewVals, RegRemap, RegRemove, RegTexAdd, RegTexEdit, BaseIniParser, GIMIObjParser, GIMIParser, IniParseBuilder, BaseIniRemover, IniRemover, IniRemoveBuilder, BasePixelTransform, ColourReplace, CorrectGamma, InvertAlpha, HighlightShadow, TempControl, TintTransform, Transparency, BaseTexFilter, GammaFilter, HueAdjust, InvertAlphaFilter, PixelFilter, TexMetadataFilter, BaseTexEditor, TexEditor, TexCreator, ModType, IfContentPart, IfPredPart, IfTemplate, IfTemplatePart, IniResourceModel, IniTexModel, Colour, ColourRange, IniSectionGraph, Mod, Model, FileStats, Version, VGRemap, Cache, LruCache, FileService, FilePath, Algo, Builder, DictTools, FlyweightBuilder, Heading, ListTools, TextTools, Logger, RemapService, remapMain

__all__ = ["Colours", "ColourConsts", "FileExt", "FileTypes", "FileEncodings", "FilePrefixes", "FileSuffixes", "FilePathConsts", "ImgFormats", "IniKeywords", "IniBoilerPlate", "GIBuilder", "IfPredPartType", "ModTypeBuilder", "ModTypes", "TexMetadataNames", "ShortCommandOpts", "CommandOpts", "HashData", "IndexData", "VGRemapData", "BadBlendData", "BlendFileNotRecognized", "ConflictingOptions", "DuplicateFileException", "Error", "FileException", "InvalidModType", "MissingFileException", "NoModType", "RemapMissingBlendFile", "Hashes", "Indices", "ModAssets", "ModIdAssets", "VGRemaps", "BlendFile", "File", "IniFile", "TextureFile", "KeepFirstDict", "BaseIniFixer", "GIMIFixer", "GIMIObjMergeFixer", "GIMIObjRegEditFixer", "GIMIObjReplaceFixer", "GIMIObjSplitFixer", "IniFixBuilder", "MultiModFixer", "BaseRegEditFilter", "RegEditFilter", "RegNewVals", "RegRemap", "RegRemove", "RegTexAdd", "RegTexEdit", "BaseIniParser", "GIMIObjParser", "GIMIParser", "IniParseBuilder", "BaseIniRemover", "IniRemover", "IniRemoveBuilder", "BasePixelTransform", "ColourReplace", "CorrectGamma", "InvertAlpha", "HighlightShadow", "TempControl", "TintTransform", "Transparency", "BaseTexFilter", "GammaFilter", "HueAdjust", "InvertAlphaFilter", "PixelFilter", "TexMetadataFilter", "BaseTexEditor", "TexEditor", "TexCreator", "ModType", "IfContentPart", "IfPredPart", "IfTemplate", "IfTemplatePart", "IniResourceModel", "IniTexModel", "Colour", "ColourRange", "IniSectionGraph", "Mod", "Model", "FileStats", "Version", "VGRemap", "Cache", "LruCache", "FileService", "FilePath", "Algo", "Builder", "DictTools", "FlyweightBuilder", "Heading", "ListTools", "TextTools", "Logger", "RemapService", "remapMain"]