# data types
# define types & conversion
# basic methods
# syntax
# define function
# operation
# for loop
# if else conditional
# while loop
# try and except block


# --------------- DATA TYPES --------------
i_am_an_integer = 1
i_am_a_float = 1.0
i_am_a_boolean = True
i_am_a_string = "SUTD"
i_am_a_list = [1,2,3]
i_am_a_tuple = (1,2,3)
i_am_a_set = {1,2,3}
i_am_a_dictionary = {"first": 1, "second": 2, "third": 3}
i_am_a_none_type = None

# --------------- TYPE CONVERSION/DEFINITION --------------
who_am_i_1_1 = int(1.5)
who_am_i_1_2 = int("1.0")  # does this work?
who_am_i_1_3 = int("1.5")  # how about this?
who_am_i_2 = float(1)
who_am_i_3_1 = bool(5)
who_am_i_3_2 = bool(0)
who_am_i_3_3 = bool(-5)  # what is the result?
who_am_i_4 = str(1)
who_am_i_5 = list({1,2,3})
who_am_i_6 = set(list(dict(x=5,y=6)))
who_am_i_7 = list(tuple(1,2,3))

# --------------- BASIC METHODS --------------
print("I love IEEE <3")  # print out the string in console
                         # print is often used to quick debugging
                         # print takes up memory, too many prints
                         # will lower the performance
                         # logger is used instead for debugging in general

print(type(1))  # find out type of your variable
print(type(i_am_a_float))  # you can refer to your defined variable like this
print("I love IEEE <3\n" + "I love SUTD <3")  # you can print multiple strings
print("I love IEEE and", i_am_a_string) # you can print different types

# user input methods
user_input = input("Enter your name: ")
print("Hello: ", user_input)

# --------------- SYNTAX --------------

# this is a useless function
def i_am_a_function(x):
    '''
    Doc string is used for clear documentation
    :param x: a useless input
    :return: True no matter what the argument is
    '''
    if x == 1:
        print("I am a useless function")
    else:
        print("I am still useless 😫")
    return True  # function without return statement will return None


# --------------- DEFINE FUNCTIONS --------------
# function can return value or simply complete an action
# function can run other functions
# you can tell a function to accept specified number of variables
# or unlimited number of variables
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def power_add(*args):
    # *args input as a list of args
    # list iteration:
    ans = 0
    for i in args:
        ans += i
    return ans

def operation_1(x,y):
    # function in function
    return add(x,substract(x,y))

# Excercise 1

# --------------- OPERATIONS --------------
print(1+1)
print(1-1)
print(2*2)
print(2**2)
print(3/2)
print(3//2)
print(3%2)

x = 1
y = x + 1
y += x  # equivalent to y = y + x
z = 5
z -= x  # equivalent to z = z - x
print(y,z)

# Excercise 2

# --------------- FOR LOOP --------------
# idea of iteration
x = [1,2,3,4,5]

def summation(l):
    result = 0
    for i in l:
        result += i
    return result

print(summation(x))


# --------------- CONDITIONAL --------------
# elif will run when if is False
# else will run when all above are False
def checker(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "ZERO"

print(checker(5))
print(checker(0))
print(checker(-10))

# Excercise 3

# --------------- WHILE LOOP --------------
# idea of infinite looping
x = 0
while 1:  # or True
    x += 1
    if x > 50:
        break  # stop the infinite looping
    else:
        continue # continue next cycle of looping
print(x)

# Excercise 4

# --------------- TRY EXCEPT --------------
# for error handling
# if error, program exit unexpectedly
# we don't want this to happen
# try-except allow us to print out error without exiting the program

user_input = input("Enter two integer separated by comma: ")
try:
    input_list = user_input.split(",")
    num1 = int(input_list[0].strip())
    num2 = int(input_list[1].strip())
    print(num1/num2)
except Exception as e:
    print("error occurred! Reason: ", e)

print("This line must be printed out successfully!!")
