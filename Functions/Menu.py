from Functions import Lang     # import language, text
from Functions import InputCSV     # Input in CSV / Data Entry
from Functions import OutputCSV     # Ausgabe Funktionen
from Functions import Topic     # Topic Funktionen



def Terminal_menu():

    print(Lang.Load_text("Menu.py", "text_1"))

    choice = input(Lang.Load_text("Menu.py", "text_2"))

    if "input" in choice:   # created entry
        InputCSV.Commandline(choice)    # to find under InputCSV
        return False   # program will not closed

    elif "output" in choice:   # print money_balance
        OutputCSV.Commandline(choice)  # to find under OutputCSV
        return False   # program will not closed

    elif "lstopic" in choice:
        Topic.ls_Commandline(choice)  # function is to find under Topic
        return False   # program will not closed

    elif "mktopic" in choice:
        Topic.mk_Commandline(choice)  # function is to find under Topic
        return False   # program will not closed

    elif "exit" in choice or "logoff" in choice:   # exit, close program
        return True    # programm will closed

    elif "help" in choice or "?" in choice:  # created entry
        print(Lang.Load_text("Menu.py", "text_3"))   # helppage
        input(Lang.Load_text("Menu.py", "text_4"))   # wait on input
        return False  # program will not closed

    else:
        print(Lang.Load_text("Menu.py", "text_5"))
        return False    # program will not closed


