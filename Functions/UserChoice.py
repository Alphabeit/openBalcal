from Functions import Lang     # import language, text
from Functions import InputCSV     # Input in CSV / Data Entry
from Functions import OutputCSV     # Ausgabe Funktionen
from Functions import Topic     # Topic Funktionen
import time    # so that output-messages do not disappear immediately



def topic_menu():

    print(Lang.Load_text("UserChoice.py", "text_1"))
    print(Lang.Load_text("UserChoice.py", "text_2") + "\n")

    choice = input(Lang.Load_text("UserChoice.py", "text_3"))

    if int(choice) == 1:   # prints all available topics
        Topic.Report_Topics()   # to find under Topic

    elif int(choice) == 2:   # crate new topic
        Topic.new_Topic()   # to find under Topic

    else:
        print(Lang.Load_text("UserChoice.py", "text_4"))
        time.sleep(3)   # sleep for 3 secs, that we can see the print



def choice_menu():

    print(Lang.Load_text("UserChoice.py", "text_5"))
    print(Lang.Load_text("UserChoice.py", "text_6"))
    print(Lang.Load_text("UserChoice.py", "text_7"))
    print(Lang.Load_text("UserChoice.py", "text_8") + "\n")

    choice = input(Lang.Load_text("UserChoice.py", "text_9"))

    if "input" in choice:   # created entry
        InputCSV.Commandline(choice)    # to find under InputCSV
        return False   # program will not closed

    elif "output" in choice:   # print money_balance
        OutputCSV.Commandline(choice)  # to find under OutputCSV
        return False   # program will not closed

    elif "lstopic" in choice:
        topic_menu()   # function is to find in this script here
        return False   # program will not closed

    elif "mktopics" in choice:
        # DEF
        return False   # program will not closed

    elif "exit" in choice or "logoff" in choice:   # exit, close program
        return True    # programm will closed

    else:
        print(Lang.Load_text("UserChoice.py", "text_4"))
        time.sleep(3)   # sleep for 3 secs, that we can see the print
        return False    # program will not closed


