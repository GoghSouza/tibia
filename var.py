import json

keyCode = {
    "F1": 0x70,
    "F2": 0x71,
    "F3": 0x72,
    "F4": 0x73,
    "F5": 0x74,
    "F6": 0x75,
    "F7": 0x76,
    "F8": 0x77,
    "F9": 0x78,
    "F10": 0x79,
    "F11": 0x7A,
    "F12": 0x7B,
    "W": 0x57,
    "S": 0x53,
    "D": 0x44,
    "A": 0x41,
    "n0": 0x60,
    "n1": 0x61,
    "n2": 0x62,
    "n3": 0x63,
    "n4": 0x64,
    "n5": 0x65,
    "n6": 0x66,
    "n7": 0x67,
    "n8": 0x68,
    "n9": 0x69,
}

def save(food, lifeRing, ringHealing, ringPlasma, collarPlasma, softBoots, tiara, runaDeath, runaFireball, runaThunder, runaAvalanche, explosiveArrow):
    my_data = {
        "food": {
            "value": food.get(),
            "position": food.current()
        },
        "life_ring": {
            "value": lifeRing.get(),
            "position": lifeRing.current()
        },
        "ring_healing": {
            "value": ringHealing.get(),
            "position": ringHealing.current()
        },   
        "ring_plasma": {
            "value": ringPlasma.get(),
            "position": ringPlasma.current()
        },
        "collar_plasma": {
            "value": collarPlasma.get(),
            "position": collarPlasma.current()
        },
        "soft_boot": {
            "value": softBoots.get(),
            "position": softBoots.current()
        },
        "tiara": {
            "value": tiara.get(),
            "position": tiara.current()
        },
        "runa_death": {
            "value": runaDeath.get(),
            "position": runaDeath.current()
        },
        "runa_fireball": {
            "value": runaFireball.get(),
            "position": runaFireball.current()
        },
        "runa_thunderstorm": {
            "value": runaThunder.get(),
            "position": runaThunder.current()
        },
        "runa_avalanche": {
            "value": runaAvalanche.get(),
            "position": runaAvalanche.current()
        },
        "explosive_arrow": {
            "value": explosiveArrow.get(),
            "position": explosiveArrow.current()
        },
    }
    with open('hotkeyRunaConfig.json', 'w') as file:
        file.write(json.dumps(my_data))
