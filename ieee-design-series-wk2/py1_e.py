# --------------- EXCERCISE 1 --------------
# make the following function complete
# copy paste into your IDE to run to test
def survey():
    name = input("What is your name?\n")
    age = input("How old are you this year?\n")
    new_age = input("How old are you after 5 years?\n")
    # something missing here

    print("Hello %s! You are %d this year." % (name, age))
    if new_age - age == 5:
        return True
    else:
        return False

if survey():
    print("Your prediction is correct!")
else:
    print("Your prediction is wrong!")


# --------------- EXCERCISE 2 --------------
# define a function named squared(x) that takes
# in an argument number x and return its squared
# value.

# your function here


# test
assert squared(5) == 25
assert squared(-3) == 9


# --------------- EXCERCISE 3 --------------
# define a function named is_squared(x,y) that takes
# in two arguments x and y
# if x is the squared value of y, return True
# otherwise return False

# your function here


# test
assert is_squared(36,6) == True
assert is_squared(12,-3) == False


# --------------- EXCERCISE 4 --------------
# complete the below function named dumb() that will keep asking
# user whether you are dumb or not. Only if the user answer
# yes will the program exits the loop and print the final
# line, otherwise, it will continue asking the same question
# over and over again

def dumb():
    # something here
        ans = input("Are you dumb?\n")
        if ans.lower().strip() == "yes":
            print("Thanks for admitting that!")
            # something here

dumb()
