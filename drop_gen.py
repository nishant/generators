import random

all_drops = 0
common_drops = 1

def drop_gen(locations):
    all_locations = [
        "Junk Junction", "Haunted Hills", "The Block",
        "Pleasant Park", "Snobby Shores", "Loot Lake",
        "Tilted Towers", "Shifty Shafts", "Polar Peak",
        "Frosty Flights", "Happy Hamlet", "Lucky Landing",
        "Fatal Fields", "Salty Springs", "Dusty Divot",
        "Paradise Palms", "Retail Row", "Lonely Lodge",
        "Sunny Steps", "Lazy Lagoon", "Pueblito",
        "Viking Village", "Soccer Field", "Greasy Lake",
        "Gus", "Volcano", "Dance Club"
    ]

    common_locations = [
        "Pleasant Park", "Dusty Divot", "Retail Row", "Salty Springs",
        "Paradise Palms", "Shifty Shafts", "Pueblito", "Viking Village"
    ]

    if locations == all_drops:
        print("Random location from all possible drops:")
        print("    " + random.choice(shuffle(all_locations)) + "\n")
    elif locations == common_drops:
        print("Random location from our common drops:")
        print("    " + random.choice(shuffle(common_locations)) + "\n")
    else:
        print("Error - Must run drop_gen(all_drops) or drop_gen(common_drops)")

def shuffle(array):
    random.shuffle(array)
    return array

drop_gen(all_drops)
drop_gen(common_drops)