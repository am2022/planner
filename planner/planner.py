import os
import datetime
from tqdm import tqdm
import time
from sys import platform
import markdown

t = datetime.datetime.now()
year = t.year
month = t.month
day = t.day

def show_option(u_os, term_color = "3f"):
    if u_os == "linux" or u_os == "osx":
        print(str(day)+" "+str(month)+" "+str(year))

        print("welcome to planner")
        print("enter -q for exit || enter -l for see list || enter -d for delete an item")
        print("enter -del for delete all the list || enter -numl for number of a work in the list")
        print("enter -count for count a work in list || enter -sort for sort the list")
        print("enter -clear for clear window || enter -hist for see history")
        print("-re for set reminder || -sort for sort the list || -color for change the color of window")
        print("-html_o for output list in html || -md_o for output list in md(markdown)")
        print("-txt_o for output list in txt file")

    elif u_os == "win":
        print(str(day)+" "+str(month)+" "+str(year))
        os.system("color 3f")

        print("welcome to planner")
        print("enter -q for exit || enter -l for see list || enter -d for delete an item")
        print("enter -del for delete all the list || enter -numl for number of a work in the list")
        print("enter -count for count a work in list || enter -sort for sort the list")
        print("enter -clear for clear window || enter -hist for see history")
        print("-re for set reminder || -sort for sort the list || -color for change the color of window")
        print("enter -html_o for output list in html || -md_o for output list in md(markdown)")
        print("-txt_o for output list in txt file")

def set_os():
    if platform == "linux" or platform == "linux2":
        return "linux"

    elif platform == "darwin":
        return "osx"

    elif platform == "win32":
        return "win"

my_os = set_os()

#os.system("cls")
if my_os == "linux" or my_os == "osx":
    os.system("clear")

elif my_os == "win":
    os.system("cls")

else:
    os_system("clear")

show_option(my_os)

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
        u_year_true = True

        print("for month or day if you want to leave blank you can enter n")

        while u_year_true:
            try:
                u_year = int(input("enter the year that you want to see history: "))
                u_year_true = False
            except:
                print("you should enter year in number format!")
                u_year_true = True

        u_month = input("enter the month: ")
        u_day = input("enter the day: ")

        if u_month == "n":
            if u_day == "n":
                f_hist = open("history "+str(year),"r")
                r = f_hist.read()
                f_hist.close()
                if r == "":
                    print("\nthe list is empty!\n")
                else:
                    print("\n")
                    print("               list:")
                    print(r)

    elif do == "-re":
        tw = input("enter the work: ")
        f = input("enter the format of time, s:sec m:minut h:hour \n")

        if f == "s":
            t = int(input("enter timer time (in second): "))

            for i in tqdm(range(1, t+1)):
                time.sleep(1)

            print("it's the time of the do "+tw+" work")

        elif f == "m":
            t = int(input("enter timer time (in minute): "))

            for i in tqdm(range(1, t*60+1)):
                time.sleep(1)

            print("it's the time of the do "+tw+" work")

        elif f == "h":
            t = int(input("enter timer time (in hour): "))

            for i in tqdm(range(1, t*60*60+1)):
                time.sleep(1)

            print("it's the time of the do "+tw+" work")

    elif do == "-sort":
        if todo == []:
            print("\nthe list is empty!\n")

        else:
            print("1.sort as alphabet 2.revers")
            sort_choice = input("enter the number of each item of the menu that you want: ")

            if sort_choice == 1 or sort_choice == "sort as alphabet":
                todo.sort()

            elif sort_choice == 2 or sort_choice == "revers":
                todo.reverse()

    elif do == "-color":
        if my_os == "win":
            print("color menu:")
            print("0 = Black       8 = Gray")
            print("1 = Blue        9 = Light Blue")
            print("2 = Green       A = Light Green")
            print("3 = Aqua        B = Light Aqua")
            print("4 = Red         C = Light Red")
            print("5 = Purple      D = Light Purple")
            print("6 = Yellow      E = Light Yellow")
            print("7 = White       F = Bright White")

            color_menu = "0123456789ABCDEF"
            color_menu = list(color_menu)

            b_color = input("enter background color:")
            b_color = b_color.upper()
            b_color_valid = False

            for i in color_menu:
                if i == b_color:
                    b_color_valid = True
                    break

            if b_color_valid:
                f_color = input("enter foreground color:")
                f_color = f_color.upper()
                f_color_valid = False

            for i in color_menu:
                    if i == f_color:
                        f_color_valid = True
                        break

            if b_color_valid and f_color_valid:
                os.system("color "+b_color+f_color)

    elif do == "-html_o":
        html_name = input("enter the name of html file(*.html):")
        md = ""

        for i in range(len(todo)):
            if i == 0:
                md = "# list"
            md += "\n* "+todo[i]

        html = markdown.markdown(md)

        with open(html_name, "w") as f_html:
            f_html.write(html)
            f_html.close()

    elif do == "-md_o":
        md_name = input("enter the name of md file(*.md):")
        md = ""

        for i in range(len(todo)):
            if i == 0:
                md = "# list"
            md += "\n* "+todo[i]

        with open(md_name, "w") as f_md:
            f_md.write(md)
            f_md.close()

    elif do == "-txt_o":
        txt_name = input("enter the name of txt file(*.txt):")
        txt = ""

        for i in range(len(todo)):
            if i == 0:
                txt = "list"
            txt += "\n\t*"+todo[i]

        with open(txt_name, "w") as f_txt:
            f_txt.write(txt)
            f_txt.close()

    else:
        todo.append(do)
        f.write(do+"\n")

try:
    f.close()
except AttributeError:
    print(" ")
