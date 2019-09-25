question = "Give a list of 5 numbers separated by commas that add up to 21\n"


def question4(grade):
    inp = input(question)
    try:
        inp_list = inp.split(",")
        if len(inp_list) == 5:
            ans = 0
            for i in inp_list:
                ans += float(i)
            if ans == 21:
                grade += 1
                return grade
            else:
                grade -= 1
                return grade
        else:
            print("Number of elements in the list does not fulfill the requirement!")
            return grade
    except Exception as e:
        print(e)
        print("Please input a valid list of nubmers as answer. Do not add any other character!")
        return grade
