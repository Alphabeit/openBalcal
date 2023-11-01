from Functions import Object   # class Objects, a dict / a case for entrys
from Functions import Lang   # Text, based on language
from Functions import Topic    # to check, if a topic from a new entry available



def Createentry(topic, date, location, info, value):   # Entry, add line

    if Topic.ifTopicAvailable(topic):   # checks if topic available, should prevent incorrect entries

        if Topic.ReportPole(topic) == "negativ":   # checks, if we have a entry (topic) where we get or lost money
            value = ("-" + value)   # negate the value
        else:   # topic is positiv
            pass   # value stay positiv

        # packs input-var's in Object / dict, just to look if it fits
        # should prevent incorrect entries
        new_entry = Object.Object(topic, date, location, info, value)

        # opens DB (CSV) for adding the new_entry
        with open("./Data/Database.csv", "a") as csv:
            #                 splits dict in tupls
            #   every key...  |
            #   |    every value from tuple (dict)
            for key, value in new_entry.asdict().items():
                csv.write(str(value) + ";")   # writes the value and a ;simicolon;
            csv.write("\n")   # finish a entry, a line with jump to the next

    else:   # if the user_topic not available
        print(Lang.Load_text("InputCSV.py", "text_1"))



def Guided_Mode():
    g_topic = input(Lang.Load_text("InputCSV.py", "text_2"))   # inputs...
    g_date = input(Lang.Load_text("InputCSV.py", "text_3"))
    g_location = input(Lang.Load_text("InputCSV.py", "text_4"))
    g_info = input(Lang.Load_text("InputCSV.py", "text_5"))
    g_value = input(Lang.Load_text("InputCSV.py", "text_6"))

    Createentry(g_topic, g_date, g_location, g_info, g_value)



def Commandline(command):   # a function to read a command, like the tools under linux/unix

    if "-h" in command or "--help" in command or "?" in command:   # return help
        print(Lang.Load_text("InputCSV.py", "text_7"))   # helppage
        input(Lang.Load_text("InputCSV.py", "text_8"))   # wait on input

    elif "-g" in command or "--guided" in command:   # start guided_mode
        Guided_Mode()

    else:   # start command

        paths = list()   # creates list, we need it soon
        given_topic = ""   # create var for topic, empty is equal no-topic, so if the user didn't give a topic, the var stay empty
        given_date = 11112233   # create var for date, also a value to control, see end of the function
        given_location = ""   # create var for location, empty is also False
        given_info = ""   # create var for info/text, empty is also False
        given_value = 99022.774   # create var for value, also a value to control, see end of the function

        flags = ("-t", "-d", "-l", "-i", "-va")   # for control

        for path in command.split(" "):   # split the command, so that we can read it
            paths.append(path)

        for x in range(len(paths)):   # for every word from our command

            if paths[x] == "-t" or paths[x] == "--topic":   # check, if we have a t-flag
                if Topic.ifTopicAvailable(paths[x+1]) and not paths[x+1] in flags:   # check, if the topic is really one of our topics, and no flag is following on a flag
                    given_topic = paths[x+1]
                else:
                    print(Lang.Load_text("InputCSV.py", "text_1"))
                    break

            elif paths[x] == "-d" or paths[x] == "--date":   # check, if we have a d-flag
                if not paths[x+1] == str and not paths[x+1] in flags:   # checks, is the date truely an integer, and no flag is following on a flag
                    given_date = paths[x+1]
                else:
                    print(Lang.Load_text("InputCSV.py", "text_9"))
                    break

            elif paths[x] == "-l" or paths[x] == "--location":   # check, if we have a l-flag
                if not paths[x+1] is None and not paths[x+1] in flags:   # checks, is a location given, and no flag is following on a flag
                    given_location = paths[x+1]
                else:
                    print(Lang.Load_text("InputCSV.py", "text_10"))
                    break

            elif paths[x] == "-i" or paths[x] == "--info":   # check, if we have a i-flag
                if not paths[x+1] is None and not paths[x+1] in flags:   # checks, is an info given, and no flag is following on a flag
                    given_info = paths[x+1]
                else:
                    print(Lang.Load_text("InputCSV.py", "text_11"))
                    break

            elif paths[x] == "-va" or paths[x] == "--value":   # check, if we have a va-flag
                 if float(paths[x+1]) and not paths[x+1] in flags:   # checks, is the value truely a float, and no flag is following on a flag
                    given_value = paths[x+1]
                 else:
                    print(Lang.Load_text("InputCSV.py", "text_12"))
                    break

            else:
                pass

        if (not given_topic == "" and   # checks, the user have all attributes given
            not given_date == 11112233 and
            not given_location == "" and
            not given_info == "" and
            not given_value == 99022.774):

            Createentry(given_topic, str(given_date), given_location, given_info, str(given_value))   # start entry

        else:   # not every attribute is set, syntax is not correctly
            print(Lang.Load_text("InputCSV.py", "text_13"))