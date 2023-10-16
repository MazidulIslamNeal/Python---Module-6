import random
def roll_dice(num):
    return random.randint(1, num)
max_num = int(input("Enter the maximum number: "))
rolls = 0

while True:
    result = roll_dice(max_num)
    rolls +=1
    if result == max_num :
        break
    print(f"Roll {rolls} : {result}")

print(f"It takes {rolls} rolls to get the maximum number ({max_num})")
