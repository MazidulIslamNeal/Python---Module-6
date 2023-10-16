import random
def roll_dice():
    return random.randint(1,6)
result = 0
rolls = 0

while result != 6:
    result = roll_dice()
    rolls += 1
    print(f"Roll {rolls}: {result}")

print(f"It took {rolls} rolls to get a 6!")
