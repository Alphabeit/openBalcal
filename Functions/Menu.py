from Functions.lowerFunctions import Lang
from Functions import InputCSV, OutputCSV, Topic



def Terminal_menu():

    command = input(Lang.Load_text("Menu.py", "text_0"))

    if "input" in command:   # created entry
        InputCSV.Commandline(command)    # to find under InputCSV
        return False   # program will not closed

    elif "output" in command:   # print money_balance
        OutputCSV.Commandline(command)  # to find under OutputCSV
        return False   # program will not closed

    elif "lstopic" in command:
        Topic.ls_Commandline(command)  # function is to find under Topic
        return False   # program will not closed

    elif "mktopic" in command:
        Topic.mk_Commandline(command)  # function is to find under Topic
        return False   # program will not closed

    elif ("exit" or "logoff") in command:   # exit, close program
        return True    # programm will closed

    elif ("help" or "?") in command:  # created entry
        print(Lang.Load_text("Menu.py", "text_1"))   # helppage
        input(Lang.Load_text("Menu.py", "text_2"))   # wait on input
        return False  # program will not closed

    else:
        print(Lang.Load_text("Menu.py", "text_3"))
        return False    # program will not closed


