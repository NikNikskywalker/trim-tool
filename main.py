import json
import os


def new_trim():
    trimName = input('Enter Trim Name: ').lower()
    trimItem = input('Enter Minecraft item to use as the template item: ')

    # DP
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
    # lang file
    langFile = {
        "trim_pattern." + packName + "." + trimName: trimName + " Armor Trim"
    }
    json_object = json.dumps(langFile, indent=4)
    with open('./' + packName + 'Resource/assets/' + packName + '/lang/en_us.json', 'w') as outfile:
        outfile.write(json_object)

    texturesList.append(packName + ":trims/models/armor/" + trimName)
    texturesList.append(packName + ":trims/models/armor/" + trimName + "_leggings")


# Pack Creation
packName = input('Enter Pack Name: ').lower()
description = input('Enter Pack Description: ')
# DP dir
os.makedirs('./' + packName + 'Data/data/' + packName + '/trim_pattern')
os.mkdir('./' + packName + 'Data/data/' + packName + '/recipes')
# DP pack.mcmeta
pack = {
    "pack": {
        "pack_format": 15,
        "description": description
    }
}
json_object = json.dumps(pack, indent=4)
with open('./' + packName + 'Data/pack.mcmeta', 'w') as outfile:
    outfile.write(json_object)
# RP dir
os.makedirs('./' + packName + 'Resource/assets/minecraft/atlases')
os.makedirs('./' + packName + 'Resource/assets/' + packName + '/textures/trims/models/armor')
os.mkdir('./' + packName + 'Resource/assets/' + packName + '/lang')
# RP pack.mcmeta
json_object = json.dumps(pack, indent=4)
with open('./' + packName + 'Resource/pack.mcmeta', 'w') as outfile:
    outfile.write(json_object)
texturesList = []

while True:
    new_trim()
    finished = input('Add more trims? (Y/N): ')
    if finished == 'Y' or finished == 'y':
        continue
    elif finished == 'N' or finished == 'n':
        break
    else:
        break

# armor trims atlas file
armorTrims = {
    "sources": [
        {
            "type": "paletted_permutations",
            "textures": texturesList,
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
