question = "What is the sum of 5 and 6.4? \n"


def question1(grade):
    inp = input(question)
    try:
        if float(inp) == 11.4:
            grade += 1
            return grade
        else:
            grade -= 1
            return grade
    except Exception as e:
        print(e)
        print("Please input a valid number as answer. Do not add any other character!")
        return grade
