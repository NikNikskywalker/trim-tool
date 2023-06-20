import json
import os

# inputs
packName = input('Enter Pack Name: ').lower()
description = input('Enter Pack Description: ')
trimName = input('Enter Trim Name: ').lower()
trimItem = input('Enter Minecraft item to use as the template item: ')

# create folders for DP and RP
# DP
DP = './' + packName + 'Data/data/' + packName + '/trim_pattern'
os.makedirs(DP)
os.mkdir('./' + packName + 'Data/data/' + packName + '/recipes')
# RP
RP = './' + packName + 'Resource/assets/minecraft/atlases'
os.makedirs(RP)
os.makedirs('./' + packName + 'Resource/assets/' + packName + '/textures/trims/models/armor')
os.mkdir('./' + packName + 'Resource/assets/' + packName + '/lang')

# DP creation
# pack.mcmeta
pack = {
    "pack": {
        "pack_format": 15,
        "description": description
    }
}
json_object = json.dumps(pack, indent=4)
with open('./' + packName + 'Data/pack.mcmeta', 'w') as outfile:
    outfile.write(json_object)

# main trim file
trimPattern = {
    "asset_id": packName + ":" + trimName,
    "description": {
        "translate": "trim_pattern." + packName + '.' + trimName
    },
    "template_item": "minecraft:" + trimItem
}
json_object = json.dumps(trimPattern, indent=4)
with open('./' + packName + 'Data/data/' + packName + '/trim_pattern/' + trimName + '.json', 'w') as outfile:
    outfile.write(json_object)

# trim recipe file
trimRecipe = {
    "type": "minecraft:smithing_trim",
    "addition": {
        "tag": "minecraft:trim_materials"
    },
    "base": {
        "tag": "minecraft:trimmable_armor"
    },
    "template": {
        "item": "minecraft:" + trimItem
    }
}
json_object = json.dumps(trimRecipe, indent=4)
with open('./' + packName + 'Data/data/' + packName + '/recipes/' + trimName + '_trim.json', 'w') as outfile:
    outfile.write(json_object)

# RP creation
# pack.mcmeta
json_object = json.dumps(pack, indent=4)
with open('./' + packName + 'Resource/pack.mcmeta', 'w') as outfile:
    outfile.write(json_object)

# lang file
langFile = {
    "trim_pattern." + packName + "." + trimName: trimName + " Armor Trim"
}
json_object = json.dumps(langFile, indent=4)
with open('./' + packName + 'Resource/assets/' + packName + '/lang/en_us.json', 'w') as outfile:
    outfile.write(json_object)

# armor trims atlas file
armorTrims = {
    "sources": [
        {
            "type": "paletted_permutations",
            "textures": [
                packName + ":trims/models/armor/" + trimName + "_1",
                packName + ":trims/models/armor/" + trimName + "_2"
            ],
            "palette_key": "trims/color_palettes/trim_palette",
            "permutations": {
                "quartz": "trims/color_palettes/quartz",
                "iron": "trims/color_palettes/iron",
                "gold": "trims/color_palettes/gold",
                "diamond": "trims/color_palettes/diamond",
                "netherite": "trims/color_palettes/netherite",
                "redstone": "trims/color_palettes/redstone",
                "copper": "trims/color_palettes/copper",
                "emerald": "trims/color_palettes/emerald",
                "lapis": "trims/color_palettes/lapis",
                "amethyst": "trims/color_palettes/amethyst"
            }
        }
    ]
}
json_object = json.dumps(armorTrims, indent=4)
with open('./' + packName + 'Resource/assets/minecraft/atlases/armor_trims.json', 'w') as outfile:
    outfile.write(json_object)
