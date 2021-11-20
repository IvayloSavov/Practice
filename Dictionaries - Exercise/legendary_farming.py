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
    key_materials = defaultdict(int)

    for i in range(0, len(inputs), 2):
        quantity, material = int(inputs[i]), inputs[i + 1].lower()
        if material in possible_items:
            key_materials[material] += quantity
            cur_value = key_materials[material]

            if cur_value >= possible_items[material]:
                print(f"{legendary_items[material]} obtained!")
                return key_materials, junk
        else:
            junk[material] += quantity


main_materials, junk_materials = separate_items()
