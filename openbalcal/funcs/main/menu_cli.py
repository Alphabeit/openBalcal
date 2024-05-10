from ..sec import inputt, output, search, topicc, report
from ..third import lang



def CLI():

    print(lang.Load_Text("menu_cli", 1))  # Welcome Message
    print(lang.Load_Text("menu_cli", 2))  # Info for Help

    for info in report.FirstMessage():   # print every report
        print(info)

    run_cli = True
    while run_cli is True:   # the real CLI, the menu

        command = input(lang.Load_Text("menu_cli", 0))

        # -------------------------------------- #
        # if-statement 01
        if "input" in command:   # created entry
            info = inputt.Commandline(command)

        elif "output" in command:   # print money_balance
            info = output.Commandline(command)

        elif "search" in command:   # search and print entrys
            info = search.Commandline(command)

        elif "lstopic" in command:   # list topics
            info = topicc.ls_Commandline(command)

        elif "mktopic" in command:   # creates topics
            info = topicc.mk_Commandline(command)

        elif "exit" in command or "logoff" in command or "quit" in command:   # exit, close program
            info = None
            run_cli = False

        elif "help" in command or "?" in command:
            info = lang.Load_Text("menu_cli", "help")

        elif command == str():   # for the case, the user use [Enter] (newline)
            info = None

        else:
            info = lang.Load_Text("menu_cli", 3)   # command not available

        # -------------------------------------- #
        # if-statement 02

        # the most time, where we get an output, if in the case of an error
        # so if we didn't get any error, we haven't anything to say
        # and didn't we have anything to say, we don't open the mouth

        if info == None:
            pass
        elif type(info) == str:
            print(info)
        else:
            for line in info:   # for list/arrays
                print(line)

        # end
        # -------------------------------------- #