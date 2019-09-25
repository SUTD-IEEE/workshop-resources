question = "What is the full name of SUTD?\n"


def question3(grade):
    inp = input(question)
    try:
        if inp.strip().lower() == "Singapore University of Technology and Design".lower():
            grade += 1
            return grade
        else:
            grade -= 1
            return grade
    except Exception as e:
        print(e)
        print("Please input a valid string as answer. Do not add any other character!")
        return grade
