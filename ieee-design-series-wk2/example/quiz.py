from questions.question1 import question1
from questions.question2 import question2
from questions.question3 import question3
from questions.question4 import question4
from questions.question5 import question5
from time import sleep


print("Welcome to QUIZARIUM!")
user_name = input("Please enter your username: \n")
grade = 0
print("Hi! {}. Your current grade is {} \nLet's begin the quiz in 5 seconds!".format(user_name, grade))
sleep(5)

# status = True
# while status:
#     new_grade = question1(grade)
#     if new_grade != grade:
#         grade = new_grade
#         print("Your grade is: ", grade)
#         print("Next question!")
#         status = False
#
# status = True
# while status:
#     new_grade = question2(grade)
#     if new_grade != grade:
#         grade = new_grade
#         print("Your grade is: ", grade)
#         print("Next question!")
#         status = False
#
# status = True
# while status:
#     new_grade = question3(grade)
#     if new_grade != grade:
#         grade = new_grade
#         print("Your grade is: ", grade)
#         print("Next question!")
#         status = False
#
# status = True
# while status:
#     new_grade = question4(grade)
#     if new_grade != grade:
#         grade = new_grade
#         print("Your grade is: ", grade)
#         print("Next question!")
#         status = False
#
# status = True
# while status:
#     new_grade = question5(grade)
#     if new_grade != grade:
#         grade = new_grade
#         print("Quiz is over! Your report is being generated!")
#         status = False

# Can it be simpler??
# The blocks above follow the similar pattern.
# What if we design another function that handle this pattern?


def quiz_operator(grade, questions):

    for question in questions:
        status = True
        while status:
            new_grade = question(grade)
            if new_grade != grade:
                grade = new_grade
                if questions.index(question) == len(questions) - 1:
                    print("Quiz is over! your report is being generated!")
                    status = False
                else:
                    print("Your grade is: ", grade)
                    print("Next question!")
                    status = False
    return grade

grade = quiz_operator(grade, [question1, question2, question3, question4, question5])


sleep(3)
print("Your final grade is: ", grade)
print("Thanks for playing!")
