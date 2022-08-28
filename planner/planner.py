import os
import datetime

os.system("cls")

t = datetime.datetime.now()
year = t.year
month = t.month
day = t.day

print(str(day)+" "+str(month)+" "+str(year))

print("welcome to planner")
print("enter -q for exit || enter -l for see list || enter -d for delete an item")
print("enter -del for delete all the list || enter -numl for number of a work in the list")
print("enter -count for count a work in list || enter -sort for sort the list")
print("enter -clear for clear window || enter -hist for see history")

f = open("history "+str(year),"a")

f.write(str(year)+" "+str(month)+" "+str(day)+"\n")

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

    elif do == "-count":
        if todo == []:
            print("\nthe list is empty!\n")
        else:
            count_work = input("enter the work: ")
            count = todo.count(count_work)

            print("the number of "+count_work+" is "+str(count))

    elif do == "-sort":
        if todo == []:
            print("\nthe list is empty!\n")
        else:
            print("1.sort as alphabet 2.revers")
            sort_choice = input("enter the number of each item of the menu that you want: ")

            if sort_choice=="1" or sort_choice=="sort as alphabet":
                todo.sort()
            elif sort_choice=="2" or sort_choice=="revers":
                todo.reverse()

    elif do == "-clear":
        os.system("cls")

    elif do == "-hist":
        print("for month or day if you want to leave blank you can enter n")
        u_year = int(input("enter the year that you want to see history: "))
        u_month = input("enter the month: ")
        u_day = input("enter the day: ")

        if u_month == "n":
            if u_day == "n":
                f_hist = open("history "+str(year),"r")
                print("\n")
                print("               list:")

                r = f_hist.read()
                print(r)
                f_hist.close()

    else:
        todo.append(do)
        f.write(do+"\n")

try:
    f.close()
except AttributeError:
    print(" ")
