from collections import defaultdict

possible_items = {
    "shards": 250,
    "fragments": 250,
    "motes": 250
}

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath",
}


def read_items():
    input_items = ""

    while True:
        line = input()
        if line == "":
            break
        input_items += line.rstrip() + " "

    return input_items


def separate_items():
    inputs = read_items().split()
    junk = defaultdict(int)
    key_materials = {
        "shards": 0,
        "motes": 0,
        "fragments": 0,
    }

    for i in range(0, len(inputs), 2):
        quantity, material = int(inputs[i]), inputs[i + 1].lower()
        if material in possible_items:
            key_materials[material] += quantity
            cur_value = key_materials[material]

            if cur_value >= possible_items[material]:
                key_materials[material] -= possible_items[material]
                print(f"{legendary_items[material]} obtained!")
                return key_materials, junk
        else:
            junk[material] += quantity


main_materials, junk_materials = separate_items()

main_materials = dict(sorted(main_materials.items(), key=lambda kvp: (-kvp[1], kvp[1])))
junk_materials = dict(sorted(junk_materials.items(), key=lambda kvp: kvp[0]))

output = {**main_materials, **junk_materials}

for item, quantity in output.items():
    print(f"{item}: {quantity}")