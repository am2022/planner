print("welcome to planner")
print("enter -q for exit || enter -l for see list || enter -d for delete an item")
print("enter -del for delete all the list || enter -numl for number of a work in the list")

todo = []

b = True

while b:
    do = input("enter work: ")

    if do == "-q":
        b = False

    elif do == "-l":
        if todo == []:
            print("\nthe list is empty!\n")
        else:
            print("               list:")
            print("\n")
            for i in todo:
                print(i)
            print("\n")

    elif do == "-d":
        if todo == []:
            print("\nthe list is empty!\n")
        else:
            print("               list:")
            print("\n")
            for i in todo:
                print(i)
            print("\n")

            d = input("which one of items you want to delete: ")

            is_dwork_valid = True

            try:
                todo.remove(d)
            except:
                print("the work is not valid!")
                is_dwork_valid = False

            if is_dwork_valid == True:
                print("done!")

    elif do == "-del":
        if todo == []:
            print("\nthe list is empty!\n")
        else:
            todo.clear()
            print("done!")

    elif do == "-numl":
        if todo == []:
            print("\nthe list is empty!\n")
        else:
            numl_work = input("enter the work: ")
            is_numl_valid = True

            try:
                numl = todo.index(numl_work)
            except:
                print("the work is not valid!")
                is_numl_valid = False

            if is_numl_valid:
                numl += 1
                print("the number of the work is in "+str(numl))

    else:
        todo.append(do)
