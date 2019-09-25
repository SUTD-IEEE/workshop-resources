from engines import game_init, bigger, smaller
from time import sleep
from random import randint
import sys

if __name__ == '__main__':
    username = game_init()
    num = randint(1, 999)  # initial guess
    lower = 1  # initial lower bound
    upper = 100  # initial upper bound
    count = 0
    guessed = {num}  # a set to store all guessed number so that we don't guess repeated numbers
    while True:
        change = input("Is it {}?\n".format(num))
        if change.lower().strip() == "lower":
            num, upper, guessed = smaller(num, lower, upper, guessed)
        elif change.lower().strip() == "higher":
            num, lower, guessed = bigger(num, lower, upper, guessed)
        elif change.lower().strip() == "yes":
            count += 1
            break
        else:
            print("I don't understand what you are saying... Please tell me either 'lower' or 'higher'.\n")
        print("Hmmm.....")
        sleep(1)
        count += 1

    print("\n\n Waaa it takes me {} rounds to get your number correctly!".format(count))
    print("Thanks for playing! {}. Hope to see you again!".format(username))
    sys.exit()
