question = "What is 121 divided by 11?\n"


def question2(grade):
    inp = input(question)
    try:
        if float(inp) == 11:
            grade += 1
            return grade
        else:
            grade -= 1
            return grade
    except Exception as e:
        print(e)
        print("Please input a valid number as answer. Do not add any other character!")
        return grade
