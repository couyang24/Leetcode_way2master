from pyfiglet import Figlet
from termcolor import cprint

sprint = lambda x: cprint(Figlet(font="standard").renderText(x), "red")

def rprint(func, lst):
    for index, item in enumerate(lst):
        result_lst = func(item)
        sprint("Example {}:".format(index + 1))
        print("********************************")
        print("The Input dataset is: {}".format(item))
        print("The Output dataset is: {}".format(result_lst))
        print("********************************")
