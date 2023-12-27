# A command is nit only a single string alone. At most, its consider a lots of flags too.
# A flag needs a lots of control-mechanics.
# Take we as example the "date". The "date" need to be a int, a value based on year_month_day, not on the alphabet or a name.
# This control-mechanics are here.

from Functions.lowerFunctions import Datevalue, Lang
from Functions import Topic



# At the beginning of the file, the flags, the syntax of the commands.
# We have a dictionary, because, so we can later control, that no flag is following on a flag.
all_syntax = {
    "h_syntax":["-h", "--help", "?", "help"],
    "g_syntax":["-g", "--guid", "--guided"],
    "t_syntax":["-t", "--topic"],
    "d_syntax":["-d", "--date"],
    "l_syntax":["-l", "--location", "--place"],
    "i_syntax":["-i", "--info", "--information"],
    "va_syntax":["-va", "--value", "--money"],
    "n_syntax":["-n", "--name", "--topicname"],
    "p_syntax":["-p", "--pole"]
}



def Flag(command, syntax):   # the flag code

    # prevent errors
    # we need for the -l & -i control a character behind the flag (in the case, -i or -l are the last character)
    # and should it has even been a blank character
    command = command + " "

    list = []   # at first, we crate a var to load our command in a list...

    for x in command.split(" "):   # ... and load our command in the list - x = path of your command
        list.append(x)

    for x2 in syntax:   # so now, we load our snytax / our searched flag in our code - x2 = searched flag from our syntax
        for x3 in range(len(list)):   # for every flag and every position in our command... - x3 = count, position of your command

            if x2 == list[x3]:   # control, if the flag is in our command...

                if list[x3+1].startswith("-"):   ### control, if the next position starts as a flag or not

                    for x4 in all_syntax:   ### if yes, we control, that the following position isnt another flag - x4 = letter_syntaxen
                        for x5 in all_syntax[x4]: ### - x5 = flags from the letter_syntaxen

                            if x5 == list[x3+1]:   ### if the following position a flag
                                return "False", Lang.Load_text("Flags.py", "text_1")   ### if yes, return False / error

                ##-## second control mechanic
                if list[x3] in all_syntax["t_syntax"]:   ##-## if your flag is an t_flag, topic
                    if Topic.ifTopicAvailable(list[x3+1]):   ##-## control, if our topic is avalible
                        return list[x3+1], "Empty"   ##-## if yes, we get the position after the flag back / "Empty" = no message is a good message
                    else:   ##-## if not
                        return "False", Lang.Load_text("Flags.py", "text_2")   ##-## we get an error

                elif list[x3] in all_syntax["d_syntax"]:   ##-## if your flga is an d_flag, date
                    try:   ##-## for date and value, we use instead of if/else, a try/except, because a int/float check deliver no true/false, neither it works or it chrash
                        int(list[x3+1])   ##-## control, if our date is made only by numbers
                        if len(list[x3+1]) == 4 or len(list[x3+1]) == 6 or len(list[x3+1]) == 8:   ##-## control, if we have a YYYY, a YYYYMM, or a YYYYMMDD
                            return list[x3+1], "Empty"
                        else:
                            return "False", Lang.Load_text("Flags.py", "text_3")   ##-## Error-Message
                    except:   ##-## if your date is a string, we can also use synonyms
                        if "today" in list[x3+1]:
                            return Datevalue.Today(), "Empty"
                        elif "yesterday" in list[x3+1]:
                            return Datevalue.Yesterday(), "Empty"
                        elif "this" in list[x3+1]:
                            if "month" in list[x3+1]:
                                return Datevalue.This_Month(), "Empty"
                            elif "year" in list[x3+1]:
                                return Datevalue.This_Year(), "Empty"
                            else:
                                return "False", Lang.Load_text("Flags.py", "text_4")  ##-## Error-Message
                        elif "last" in list[x3+1]:
                            if "month" in list[x3+1]:
                                return Datevalue.Last_Month(), "Empty"
                            elif "year" in list[x3+1]:
                                return Datevalue.Last_Year(), "Empty"
                            else:
                                return "False", Lang.Load_text("Flags.py", "text_4")  ##-## Error-Message
                        else:
                            return "False", Lang.Load_text("Flags.py", "text_4")   ##-## Error-Message

                elif list[x3] in all_syntax["l_syntax"]:   ##-## l_flag, location
                    if not list[x3+1] == "":   ##-## control, if our location is not empty
                        return list[x3+1], "Empty"
                    else:
                        return "False", Lang.Load_text("Flags.py", "text_5")   ##-## Error-Message

                elif list[x3] in all_syntax["i_syntax"]:   ##-## i_flag, info
                    if not list[x3+1] == "":  ##-## control, if our info is not empty
                        return list[x3+1], "Empty"
                    else:
                        return "False", Lang.Load_text("Flags.py", "text_6")   ##-## Error-Message

                elif list[x3] in all_syntax["va_syntax"]:   ##-## va_flag, value
                    try:
                        float(list[x3+1])   ##-## control, if our value is made only by numbers
                        return list[x3+1], "Empty"
                    except:
                        return "False", Lang.Load_text("Flags.py", "text_7")   ##-## Error-Message

                elif list[x3] in all_syntax["n_syntax"]:   ##-## n_flag, name, import for create topic
                    if not Topic.ifTopicAvailable(list[x3+1]):   ##-## control, if your new topic is not available, prevent duplicates
                        return list[x3+1], "Empty"
                    else:
                        return "False", Lang.Load_text("Flags.py", "text_8")   ##-## Error-Message

                elif list[x3] in all_syntax["p_syntax"]:   ##-## p_flag, pole, important for create topic
                    if list[x3+1] == "+" or list[x3+1] == "plus" or list[x3+1] == "add":   ##-## control, if your pole is positiv
                        return "positiv", "Empty"
                    elif list[x3+1] == "-" or list[x3+1] == "minus" or list[x3+1] == "less":   ##-## control, if your pole is negative
                        return "negativ", "Empty"
                    else:
                        return "False", Lang.Load_text("Flags.py", "text_9")   ##-## Error-Message

                else:   ##-## should not happen, is an error
                    return "False", "Unknowen-Error"

            else:   ### if not, we are going to the next position
                pass

    return "False, Flag is missing", Lang.Load_text("Flags.py", "text_10")    # if our flag is not in the command, return False / error



##################################### the command flags
def h_Flag(command):   # help

    for x in all_syntax["h_syntax"]:
        if x in command:
            return True

        else:
            pass



def g_Flag(command):   # guid-mode

    for x in all_syntax["g_syntax"]:
        if x in command:
            return True

        else:
            pass



def t_Flag(command):   # topic
    return Flag(command, all_syntax["t_syntax"])



def d_Flag(command):   # date
    date, message = Flag(command, all_syntax["d_syntax"])

    if "missing" in str(date):   # if no date given
        date = Datevalue.Today()   # use today
        message = "Empty"
    else:
        pass

    return date, message



def l_Flag(command):   # location
    return Flag(command, all_syntax["l_syntax"])



def i_Flag(command):   # info
    return Flag(command, all_syntax["i_syntax"])



def va_Flag(command):   # value
    return Flag(command, all_syntax["va_syntax"])



def n_Flag(command):   # name
    return Flag(command, all_syntax["n_syntax"])



def p_Flag(command):   # pole
    return Flag(command, all_syntax["p_syntax"])