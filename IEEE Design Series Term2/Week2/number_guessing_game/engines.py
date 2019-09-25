from time import sleep
from random import randint


def game_init():
    """
    This is the initialization of the game. It will only be run once.
    :return: user's name
    """

    name = input("Hi! Welcome to GUESS WHAT NUMBER IT IS! Please tell me your name: ")
    print("\nHi! {}. Now let me explain the instructions to you.\n".format(name))
    sleep(1)
    print("Think of an integer range from 1 to 999 in your mind.")
    sleep(1)
    print("I will then give you a number of my guess.")
    sleep(1)
    print("If it is bigger than yours, tell me to go lower by entering LOWER.")
    sleep(1)
    print("If it is smaller, please enter HIGHER to tell me to guess bigger number.")
    sleep(1)
    print("If it is correct, please tell me by saying 'yes'!")
    sleep(1)
    print("I will try my best to guess the number you think of and tell you how many rounds I take to guess it correctly.\n")
    sleep(2)
    print("Alright! Let's begin!")
    sleep(1)
    print("Now think of an integer from 1 to 999 in your mind. Don't tell me!")
    sleep(3)
    print("You done? OK let me guess...")
    return name


def smaller(num, lower, upper, guessed):
    """
    run this when user answer LOWER
    :param num: previous guessed number
    :param lower: previous lower bound
    :param upper: previous upper bound
    :param guessed: set of numbers guessed
    :return: new randint num generated, new upper bound, new guessed set
    """
    upper = num  # update upper bound
    while True:
        new_num = randint(lower, upper)
        if new_num not in guessed:
            guessed.add(new_num)
            break
    return new_num, upper, guessed


def bigger(num, lower, upper, guessed):
    """
    run this when user answer HIGHER
    :param num: previous guessed number
    :param lower: previous lower bound
    :param upper: previous upper bound
    :param guessed: set of numbers guessed
    :return: new randint num generated, new lower bound, new guessed set
    """

    lower = num  # update lower bound
    while True:
        new_num = randint(lower, upper)
        if new_num not in guessed:
            guessed.add(new_num)
            break
    return new_num, lower, guessed
