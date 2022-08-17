print("welcome to planner")
print("enter -q for exit || enter -l for see list")

todo = []

b = True

while b:
    do = input("enter work: ")

    if do == "-q":
        b = False

    elif do == "-l":
        print("               list:")
        print("\n")

        for i in todo:
            print(i)

        print("\n")

    else:
        todo.append(do)
