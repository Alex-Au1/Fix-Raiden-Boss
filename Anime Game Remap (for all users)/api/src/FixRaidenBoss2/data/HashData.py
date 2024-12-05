##### Credits

# ===== Anime Game Remap (AG Remap) =====
# Authors: NK#1321, Albert Gold#2696
#
# if you used it to remap your mods pls give credit for "Nhok0169" and "Albert Gold#2696"
# Special Thanks:
#   nguen#2011 (for support)
#   SilentNightSound#7430 (for internal knowdege so wrote the blendCorrection code)
#   HazrateGolabi#1364 (for being awesome, and improving the code)

##### EndCredits


##### Script
HashData = HashData = {4.0 : {"Amber": {"draw_vb": "870a7499", "position_vb": "caddc4c6", "blend_vb": "ca5bd26e", "texcoord_vb": "e3047676", "ib": "9976d124",
                 "tex_head_diffuse": "ae27902d", "tex_head_lightmap": "29b001ba", "tex_head_shadowramp": "7eb5b84e",
                 "tex_body_diffuse": "bc86882f", "tex_body_lightmap": "9e1294dd", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                 "tex_face_diffuse": "1d064079", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "AmberCN": {"draw_vb": "da0adf2f", "position_vb": "7f94e8da", "blend_vb": "f35340d5", "texcoord_vb": "dbc594b6", "ib": "8cc9274b",
                    "tex_head_diffuse": "ae27902d", "tex_head_lightmap": "29b001ba", "tex_head_shadowramp": "7eb5b84e",
                    "tex_body_diffuse": "f683bcac", "tex_body_lightmap": "69b6e698", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                    "tex_face_diffuse": "1d064079", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "Barbara": {"draw_vb": "f41c47cf", "position_vb": "85282151", "blend_vb": "22a31278", "texcoord_vb": "0f18519e", "ib": "231723d2",
                    "tex_head_diffuse": "d9d24fbf", "tex_head_lightmap": "f89f1ed6", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                    "tex_body_diffuse": "d5fd9da6", "tex_body_lightmap": "0c0ce0ef", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                    "tex_dress_diffuse": "d5fd9da6", "tex_dress_lightmap": "0c0ce0ef", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                    "tex_face_diffuse": "d9f80241", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "BarbaraSummertime": {"draw_vb": "60fcbabe", "position_vb": "8b9e7c22", "blend_vb": "639d62b6", "texcoord_vb": "27057f58", "ib": "a411cfbc",
                    "tex_head_diffuse": "fa94dcc6", "tex_head_lightmap": "07b96e90", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                    "tex_body_diffuse": "fa78e66c", "tex_body_lightmap": "a8eec489", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                    "tex_dress_diffuse": "fa78e66c", "tex_dress_lightmap": "a8eec489", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                    "tex_face_diffuse": "72a0dee8", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "Fischl": {"draw_vb": "6c491d3b", "position_vb": "9838aedf", "blend_vb": "0d1c1932", "texcoord_vb": "d451d8d8", "ib": "5cfc7a92",
                   "tex_head_diffuse": "8b7f4637", "tex_head_lightmap": "3b8e30d7", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "9f758879", "tex_body_lightmap": "3c5e7327", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "59cd2559",
                   "tex_dress_diffuse": "9f758879", "tex_dress_lightmap": "3c5e7327", "tex_dress_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "0cd456af", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398"},
        "FischlHighness": {"draw_vb": "3cc8f82b", "position_vb": "8f473224", "blend_vb": "dbd6a5c3", "texcoord_vb": "a800a294", "ib": "95bf8d7e",
                   "tex_head_diffuse": "de37696a", "tex_head_lightmap": "2f2f6932", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "a132243b", "tex_body_lightmap": "61c02f66", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "0cd456af", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "Ganyu": {"draw_vb": "721ca964", "position_vb": "a5169f1d", "blend_vb": "6f47a39d", "texcoord_vb": "cf27251f", "ib": "2da186bc",
                  "tex_head_diffuse": "6d78ac96", "tex_head_lightmap": "9b0d2126", "tex_head_shadowramp": "7eb5b84e",
                  "tex_body_diffuse": "8a151913", "tex_body_lightmap": "dbcf1d72", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                  "tex_dress_diffuse": "8a151913", "tex_dress_lightmap": "dbcf1d72", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                  "tex_face_diffuse": "b2657593", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "Jean": {"draw_vb": "e6055135", "position_vb": "191af650", "blend_vb": "3cb8153c", "texcoord_vb": "1722136c", "ib": "29835d20",
                 "tex_head_diffuse": "dba2791d", "tex_head_lightmap": "0bd77e81", "tex_head_shadowramp": "7eb5b84e",
                 "tex_body_diffuse": "d1ae8efe", "tex_body_lightmap": "cee17ba5", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                 "tex_face_diffuse": "c2d1a57e", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "JeanCN": {"draw_vb": "2a29e333", "position_vb": "93bb2522", "blend_vb": "d159bf31", "texcoord_vb": "0ffefb98", "ib": "920c0b3f",
                   "tex_head_diffuse": "6eca0f93", "tex_head_lightmap": "92ed604c", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "0f9c7705", "tex_body_lightmap": "617c45a0", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "c2d1a57e", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "JeanSea": {"draw_vb": "972d56ee", "position_vb": "16fef1eb", "blend_vb": "ac801371", "texcoord_vb": "3ffb0363", "ib": "5114a891",
                   "tex_head_diffuse": "3b4efe72", "tex_head_lightmap": "4b8a3da9", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "e555db10", "tex_body_lightmap": "15671abb", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_dress_diffuse": "e555db10", "tex_dress_lightmap": "15671abb", "tex_dress_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "c2d1a57e", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "Keqing": {"draw_vb": "4526145e", "position_vb": "3aaf3e94", "blend_vb": "0bf8e621", "texcoord_vb": "723848fe", "ib": "f325e394",
                   "tex_head_diffuse": "58de714b", "tex_head_lightmap": "da3e4a28", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "874b8c0b", "tex_body_lightmap": "0695efb7", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_dress_diffuse": "874b8c0b", "tex_dress_lightmap": "0695efb7", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "d8c9c399", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "KeqingOpulent": {"draw_vb": "efcc8769", "position_vb": "0d7e3cc5", "blend_vb": "6f010b58", "texcoord_vb": "52f78cb7", "ib": "44bba21c",
                   "tex_head_diffuse": "e2d7ae66", "tex_head_lightmap": "13e2b0ab", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "2af5bf71", "tex_body_lightmap": "195af53a", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "c2b17f84", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_shadowramp": "7eb5b84e"},
        "Kirara": {"draw_vb": "e656b9fd", "position_vb": "cc833025", "blend_vb": "01d54938", "texcoord_vb": "33b3d6e5", "ib": "ce3dc5a2",
                   "tex_head_normalmap": "6006d89d", "tex_head_diffuse": "0998fcda", "tex_head_lightmap": "c90298cc", "tex_head_metalmap": "b0e08915",
                   "tex_body_normalmap": "acf97111", "tex_body_diffuse": "9feba8b9", "tex_body_lightmap": "2fadf527", "tex_body_metalmap": "b0e08915",
                   "tex_dress_normalmap": "acf97111", "tex_dress_diffuse": "9feba8b9", "tex_dress_lightmap": "2fadf527", "tex_dress_metalmap": "b0e08915",
                   "tex_face_normalmap": "6eb20522", "tex_face_diffuse": "4e3376db", "tex_face_lightmap": "30180763"},
        "Mona": {"draw_vb": "00741928", "position_vb": "20d0bfab", "blend_vb": "52f0e9a0", "texcoord_vb": "a8191396", "ib": "ef876207",
                 "tex_head_diffuse": "b518c5a5", "tex_head_lightmap": "0c679d22", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                 "tex_body_diffuse": "5f873d89", "tex_body_lightmap": "29d50a21", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                 "tex_face_diffuse": "8e116301", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "MonaCN": {"draw_vb": "41f18240", "position_vb": "ee5ed1dc", "blend_vb": "bad2731b", "texcoord_vb": "e543af5d", "ib": "ed79ea5b",
                   "tex_head_diffuse": "0320a4d2", "tex_head_lightmap": "df0f8b90", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "c043f913", "tex_body_lightmap": "a3369d08", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "8e116301", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "Nilou":  {"draw_vb": "2f95abf6", "position_vb": "b2acc1df", "blend_vb": "fda8e783", "texcoord_vb": "583fba29", "ib": "265e34e3",
                   "tex_head_normalmap": "6f0680d3", "tex_head_diffuse": "9caa70ad", "tex_head_lightmap": "b2501b97", "tex_head_metalmap": "b0e08915",
                   "tex_body_normalmap": "a87ce1c0", "tex_body_diffuse": "91cb97a8", "tex_body_lightmap": "29cf0914", "tex_body_metalmap": "b0e08915",
                   "tex_dress_normalmap": "a87ce1c0", "tex_dress_diffuse": "91cb97a8", "tex_dress_lightmap": "29cf09   14", "tex_dress_metalmap": "b0e08915",
                   "tex_face_diffuse": "0957b10f", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "3f396398", "tex_face_metalmap": "b0e08915"},
        "Ningguang": {"draw_vb": "e4fc5902", "position_vb": "55b43e99", "blend_vb": "9f7dc19c", "texcoord_vb": "906ad233", "ib": "93085db7",
                   "tex_head_diffuse": "e0789f0d", "tex_head_lightmap": "5d182ae7", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "5ffe95c2", "tex_body_lightmap": "64e6b893", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_dress_diffuse": "5ffe95c2", "tex_dress_lightmap": "64e6b893", "tex_dress_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "4cc85338", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "NingguangOrchid": {"draw_vb": "10de9c78", "position_vb": "db37b198", "blend_vb": "a8246d4a", "texcoord_vb": "396aa3ec", "ib": "f1d09b47",
                   "tex_head_diffuse": "b68d7488", "tex_head_lightmap": "bc1034dd", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "a4597b85", "tex_body_lightmap": "0e26784e", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_dress_diffuse": "a4597b85", "tex_dress_lightmap": "0e26784e", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "4cc85338", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "Raiden": {"draw_vb": "a05e7bec", "position_vb": "e48c61f3", "blend_vb": "1a495487", "texcoord_vb": "0c37fc86", "ib": "428c56cd"},
        "RaidenBoss": {"blend_vb": "fe5c0180"},
        "Rosaria": {"draw_vb": "9e1868d9", "position_vb": "748f40a5", "blend_vb": "4de959bd", "texcoord_vb": "06b8fbf5", "ib": "5d18b9d6",
                    "tex_head_diffuse": "81b2d0ca", "tex_head_lightmap": "2f19c547", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                    "tex_body_diffuse": "9abde85f", "tex_body_lightmap": "743ffc09", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                    "tex_dress_diffuse": "81b2d0ca", "tex_dress_lightmap": "2f19c547", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                    "tex_extra_diffuse": "9abde85f", "tex_extra_lightmap": "743ffc09", "tex_extra_metalmap": "b0e08915", "tex_extra_shadowramp": "7eb5b84e",
                    "tex_face_diffuse": "2abd61ee", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "RosariaCN": {"draw_vb": "f3d4a01a", "position_vb": "59a1f8b1", "blend_vb": "a7bee046", "texcoord_vb": "86e0d16b", "ib": "851e4de1",
                      "tex_head_diffuse": "55280cb0", "tex_head_lightmap": "825c32a0", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                      "tex_body_diffuse": "bd6fcf34", "tex_body_lightmap": "cf7b6deb", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                      "tex_dress_diffuse": "55280cb0", "tex_dress_lightmap": "825c32a0", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                      "tex_extra_diffuse": "bd6fcf34", "tex_extra_lightmap": "cf7b6deb", "tex_extra_metalmap": "b0e08915", "tex_extra_shadowramp": "7eb5b84e",
                      "tex_face_diffuse": "2abd61ee", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"},
        "Shenhe": {"draw_vb": "fde191d7", "position_vb": "e44b58b5", "blend_vb": "541cf273", "texcoord_vb": "86c4f5ec", "ib": "0b7d4e4d",
                   "tex_head_diffuse": "7da9c07b", "tex_head_lightmap": "e134c758", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "7eb5b84e",
                   "tex_body_diffuse": "cba1d6ec", "tex_body_lightmap": "ce5176af", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "7eb5b84e",
                   "tex_dress_diffuse": "cba1d6ec", "tex_dress_lightmap": "ce5176af", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "7eb5b84e",
                   "tex_face_diffuse": "f5f393cb", "tex_face_lightmap": "4e3376db", "tex_face_shadow": "bf9fccca", "tex_face_shadowramp": "7eb5b84e"}},
4.1 : {"Amber": {"draw_vb":"0eef5bbe"},
       "AmberCN": {"draw_vb":"53eff008"},
       "Barbara": {"draw_vb": "7df968e8"},
       "BarbaraSummertime": {"draw_vb": "e9199599"},
       "Fischl": {"draw_vb":"e5ac321c"},
       "FischlHighness": {"draw_vb": "b52dd70c"},
       "Ganyu": {"draw_vb": "fbf98643"},
       "Jean": {"draw_vb":"6fe07e12"},
       "JeanCN": {"draw_vb":"a3cccc14"},
       "JeanSea": {"draw_vb": "1ec879c9"},
       "Keqing": {"draw_vb": "ccc33b79"},
       "KeqingOpulent": {"draw_vb": "6629a84e"},
       "Kirara": {"draw_vb": "6fb396da"},
       "Mona": {"draw_vb":"8991360f"},
       "MonaCN": {"draw_vb":"c814ad67"},
       "Nilou": {"draw_vb": "a67084d1"},
       "Ningguang": {"draw_vb": "6d197625"},
       "NingguangOrchid": {"draw_vb": "993bb35f"},
       "Raiden": {"draw_vb":"29bb54cb"},
       "Rosaria": {"draw_vb":"17fd47fe"},
       "RosariaCN": {"draw_vb":"7a318f3d"},
       "Shenhe": {"draw_vb": "7404bef0"}},
4.3 : {"Amber": {"ib":"a1a2bbfb"},
       "Barbara": {"ib": "1bc3490d"},
       "BarbaraSummertime": {"ib": "9cc5a563"},
       "AmberCN": {"ib":"b41d4d94"},
       "Fischl": {"ib": "6428104d"},
       "FischlHighness": {"ib": "ad6be7a1"},
       "Ganyu": {"ib": "1575ec63"},
       "Jean": {"ib":"115737ff"},
       "JeanCN": {"ib":"aad861e0"},
       "JeanSea": {"ib": "69c0c24e"},
       "Keqing": {"ib": "cbf1894b"},
       "KeqingOpulent": {"ib": "7c6fc8c3"},
       "Kirara": {"ib": "f6e9af7d"},
       "Mona": {"ib":"d75308d8"},
       "MonaCN": {"ib":"d5ad8084"},
       "Nilou": {"ib": "1e8a5e3c"},
       "Ningguang": {"ib": "abdc3768"},
       "NingguangOrchid": {"ib":"c904f198"},
       "Raiden": {"ib":"7a583c12"},
       "Rosaria": {"ib":"65ccd309"},
       "RosariaCN": {"ib":"bdca273e"},
       "Shenhe": {"ib": "33a92492"}},
4.4 : {"Amber": {"position_vb": "a2ea4b2d", "blend_vb": "36d20a67", "texcoord_vb": "81b777ca", "ib": "b03c7e30"},
       "AmberCN": {"position_vb": "557b2eff"},
       "Fischl": {"position_vb": "bf6aef4d"},
       "Mona": {"position_vb": "7a1dc890", "blend_vb": "b043715a"},
       "MonaCN": {"position_vb": "515f3ce6"},
       "Ningguang": {"draw_vb": "4c2f9a0a", "position_vb": "f9e1b52b", "blend_vb": "735eaea4", "texcoord_vb": "1f0ab400", "ib": "ad75352c"},
       "ShenheFrostFlower": {"draw_vb": "6102c3ef", "position_vb": "ee0980eb", "blend_vb": "263019b8", "texcoord_vb": "d36f368d", "ib": "83a9116d",
                             "tex_head_normalmap": "4e5d638d", "tex_head_diffuse": "1ab2f510", "tex_head_lightmap": "b0e08915", "tex_head_shadowramp": "58d2635b",
                             "tex_body_normalmap": "625d0bb4", "tex_body_diffuse": "51529edd", "tex_body_lightmap": "b0e08915", "tex_body_shadowramp": "58d2635b",
                             "tex_dress_normalmap": "4e5d638d", "tex_dress_diffuse": "1ab2f510", "tex_dress_lightmap": "7eb5b84e", "tex_dress_shadowramp": "000050-ps-t3", # is the hash for "tex_dress_shadowramp" even valid? reference: https://github.com/SilentNightSound/GI-Model-Importer-Assets/commit/79d40a4d4708500f44035ade5a6be6c5d6cb0285#diff-2f0914f9ffdcb1e85d8a1e64ba1f12bc7521da3a7f184a2c2eccbaeb702c9290
                             "tex_extra_normalmap": "625d0bb4", "tex_extra_diffuse": "51529edd", "tex_extra_lightmap": "7eb5b84e", "tex_extra_shadowramp": "000049-ps-t3"},
       "GanyuTwilight": {"draw_vb": "1ad9c181", "position_vb": "9b3f356e", "blend_vb": "9a5c01d2", "texcoord_vb": "5ff2f1d1", "ib": "cb283c86",
                         "tex_head_normalmap": "f8aa8a9d", "tex_head_diffuse": "ad1ed796", "tex_head_lightmap": "191ebe05", "tex_head_metalmap": "b0e08915",
                         "tex_body_normalmap": "e304bdcf", "tex_body_diffuse": "13fa0b53", "tex_body_lightmap": "b0e08915", "tex_body_shadowramp": "58d2635b",
                         "tex_dress_normalmap": "e304bdcf", "tex_dress_diffuse": "13fa0b53", "tex_dress_lightmap": "b0e089    15", "tex_dress_shadowramp": "58d2635b"},
       "Kirara": {"position_vb": "b57d7fe2"}},
4.6 : {"Arlecchino" : {"draw_vb": "44e3487a", "position_vb": "6895f405", "blend_vb": "e211de60", "texcoord_vb": "8b17a419", "ib": "e811d2a1"},
       "ArlecchinoBoss": {"draw_vb": "970e7336", "position_vb": "cf66bef6", "blend_vb": "5227c79e", "texcoord_vb": "a75e7052", "ib": "480f1267"}},
4.8 : {"NilouBreeze": {"draw_vb": "3f79fabb", "position_vb": "7d53d78f", "blend_vb": "49bede49", "texcoord_vb": "b976b848", "ib": "00439fbb",
                   "tex_head_diffuse": "2593dea6", "tex_head_lightmap": "3f78afbf", "tex_head_metalmap": "b0e08915", "tex_head_shadowramp": "58d2635b",
                   "tex_body_diffuse": "9f7e392b", "tex_body_lightmap": "e3e73b29", "tex_body_metalmap": "b0e08915", "tex_body_shadowramp": "58d2635b", 
                   "tex_dress_diffuse": "9f7e392b", "tex_dress_lightmap": "e3e73b29", "tex_dress_metalmap": "b0e08915", "tex_dress_shadowramp": "58d2635b"},
        "KiraraBoots": {"draw_vb": "4955fc99", "position_vb": "f8013ba9", "blend_vb": "53a2502b", "texcoord_vb": "596e8fe0", "ib": "846979e2",
                   "tex_head_normalmap": "c715bcf7", "tex_head_diffuse": "16fbe9b0", "tex_head_lightmap": "f74f093d", "tex_head_metalmap": "b0e08915",
                   "tex_body_normalmap": "89a118ba", "tex_body_diffuse": "e3a21e6f", "tex_body_lightmap": "8ca27fd3", "tex_body_metalmap": "b0e08915",
                   "tex_dress_normalmap": "e3a21e6f", "tex_dress_diffuse": "8ca27fd3", "tex_dress_lightmap": "7eb5b84e", "tex_dress_metalmap": "b0e08915"}}}
##### EndScript