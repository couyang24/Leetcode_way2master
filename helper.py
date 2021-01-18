from pyfiglet import Figlet
from termcolor import cprint
from icecream import ic

sprint = lambda x: cprint(Figlet(font="standard").renderText(x), "red")

def rprint(func, lst, outputs=[]):
    for index, item in enumerate(lst):
        result = func(item)
        sprint("Example {}:".format(index + 1))
        print("********************************")
        print("The Input dataset is: {}".format(item))
        if outputs == []:
            print("The Output dataset is: {}.".format(result))
        else:
            print("The Output dataset is: {} and the correct answer is also {}.".format(result, outputs[index]))
            assert result == outputs[index], "The results do not match"
        print("********************************")

def rprint2(func, lst1, lst2, outputs=[]):
    for index in range(len(lst1)):
        result = func(lst1[index], lst2[index])
        sprint("Example {}:".format(index + 1))
        print("********************************")
        print("The Input dataset is: {} & {}".format(lst1[index], lst2[index]))
        if outputs == []:
            print("The Output dataset is: {}.".format(result))
        else:
            print("The Output dataset is: {} and the correct answer is also {}.".format(result, outputs[index]))
            assert result == outputs[index], "The results do not match"
        print("********************************")
