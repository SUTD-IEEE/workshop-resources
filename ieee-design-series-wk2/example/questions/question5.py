question = "What is your favourite club in SUTD?\n"


def question5(grade):
    inp = input(question)
    try:
        inp = inp.strip().lower()
        if inp == "ieee" or inp == "ieee sutd" or inp == "ieee sutd student branch":
            grade += 1
            return grade
        else:
            grade -= 1
            return grade
    except Exception as e:
        print(e)
        print("Please input a valid string as answer. Do not add any other character!")
        return grade
