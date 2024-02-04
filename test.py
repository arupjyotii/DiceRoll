import random

def roll_dice():

    dice_result = random.randint(1, 6)

    # Print statements based on the outcome
    if dice_result == 1:
        print("Program 1")
    elif dice_result == 2:
        print("Program 2")
    elif dice_result == 3:
        print("Program 3")
    elif dice_result == 4:
        print("Program 4")
    elif dice_result == 5:
        print("Program 5")
    elif dice_result == 6:
        print("Program 6")

if __name__ == "__main__":
    roll_dice()
