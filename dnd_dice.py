import random
import sys


def roll_dice(amount, dice):
    results = [  # Generate numbers between [1, dice]
        random.randint(1, dice)
        for n
        in range(amount)]
    return results  # Return the results in a list.


def run_dice():

    loop = 1  # Asks if you want to use a modifier
    yes = ["yes", "y"]
    no = ["no", "n"]
    stop = ["quit", "q"]
    while loop == 1:
        print("\nRoll dice with modifier?")
        answer_1 = input()
        if answer_1 in yes:
            loop = 3
        elif answer_1 in no:
            loop = 2
        elif answer_1 in stop:
            print("\nGoodbye, Homie!\n")
            sys.exit()
        else:
            print("\nTry again")
            loop = 1

    while loop == 2:  # Dice roll without modifier
        try:
            dice = int(input("\nWhat dice would you like to throw? >> "))
            amount = int(input("\nHow many of those dice? >> "))
        except ValueError:
            print("\nPlease enter a valid input")
            continue
        else:
            print("\n")
            print()
            dice_roll = [0, 0]
            dice_roll = (roll_dice(int(amount), int(dice)))
            print(dice_roll)
            print("\n")
            summary = sum(dice_roll)
            print(f"\nThe total of the dice is {summary}")
            loop = 1
            run_dice()

    while loop == 3:  # Dice roll with modifier
        try:
            dice = int(input("\nWhat dice would you like to throw? >> "))
            amount = int(input("\nHow many of those dice? >> "))
            modifier = int(input("\nWhat is the modifier? >> "))
        except ValueError:
            print("\nPlease enter a valid input")
            continue
        else:
            print("\n")
            print()
            dice_roll = []
            mod_adjuster = []
            mod_adjuster.append(modifier)
            dice_roll = (roll_dice(int(amount), int(dice)))
            # makes two lists, one with the rolls and the modifier
            print(dice_roll)
            print(mod_adjuster)
            # adds all rolls and modifier together in list
            dice_roll.append(modifier)
            print("\n")
            summary = sum(dice_roll)  # sum of rolls and modifier
            print(f"\nThe total of the dice with the modifier is {summary}")
            # print("\n")
            loop = 1
            run_dice()


run_dice()
