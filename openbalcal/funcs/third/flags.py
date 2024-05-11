# A command is not only a single string. It is a lots of single parts, split by flags.
# A flag needs a lots of control-mechanics.
# Take we as example the "date". The "date" need to be an int, a value based on year_month_day, not on the alphabet or a name.
# This control-mechanics are built here.

from ..sec import topicc
from ..third import lang, dategen
import re, datetime



# At the beginning of the file, the flags, the syntax of the commands.
# We have a dictionary, because, so we can prove later, that no flag is following on another flag.
all_syntax = {
    "h_syntax":["-h", "--help", "?", "help"],
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
    # for a successful control, we need a blank behind the last character (in the case, -i or -l are the last character)
    command = "{} ".format(command)

    list = []   # to split the command in a list

    for x in command.split(" "):   # split text in strings
        list.append(x)

    for x2 in syntax:   # syntax / x2 = searched flag
        for x3 in range(len(list)):   # for every string in our command

            if x2 == list[x3]:   # if searched flag found

                # ---------------------------- #
                # control, no flag is following on another flag
                if list[x3+1].startswith("-"):

                    for x4 in all_syntax:   # any flag-syntax
                        for x5 in all_syntax[x4]:    # any flag from any flag-syntax

                            if x5 == list[x3+1]:   # if string after flag another flag
                                return False, lang.Load_Text("flags", 1)
                # end
                # ---------------------------- #

                # -------------------------------------- #
                # topic
                if list[x3] in all_syntax["t_syntax"]:   # if your flag is an t_flag
                    if topicc.ifTopicAvailable(list[x3+1]):   # control, if our topic is available
                        return True, list[x3+1]
                    else:
                        return False, lang.Load_Text("flags", 2)

                # -------------------------------------- #
                # date
                elif list[x3] in all_syntax["d_syntax"]:

                    if re.findall("[0-9]", list[x3+1]) and not re.findall("[a-zA-Z]", list[x3+1]):   # in case of date int
                        if len(list[x3+1]) == 4 or len(list[x3+1]) == 6 or len(list[x3+1]) == 8:   # YYYY, YYYYMM, or YYYYMMDD
                            return True, list[x3+1]
                        else:
                            return False, lang.Load_Text("flags", 3)

                    elif re.findall("[a-zA-Z]", list[x3+1]) and not re.findall("[0-9]", list[x3+1]):   # in case of synonyms
                        nr_alias, date = dategen.DateAliasSwitch(list[x3 + 1])

                        if re.findall("[1-6]", str(nr_alias)):
                            return True, date

                        else:   # nr_alias is 7, Err
                            return False, lang.Load_Text("flags", 4)

                    else:   # in case no int, no str
                        return False, lang.Load_Text("flags", 5)

                # -------------------------------------- #
                # location
                elif list[x3] in all_syntax["l_syntax"]:
                    if not list[x3+1] == str():   # control is not empty
                        return True, list[x3+1]
                    else:
                        return False, lang.Load_Text("flags", 6)

                # -------------------------------------- #
                # info
                elif list[x3] in all_syntax["i_syntax"]:
                    if not list[x3 + 1] == str():
                        return True, list[x3 + 1]
                    else:
                        return False, lang.Load_Text("flags", 7)

                # -------------------------------------- #
                # value
                elif list[x3] in all_syntax["va_syntax"]:
                    if re.findall("[0-9]", list[x3+1]) and not re.findall("[a-zA-Z]", list[x3+1]):
                        return True, float(list[x3+1])
                    else:
                        return False, lang.Load_Text("flags", 8)

                # -------------------------------------- #
                # name
                elif list[x3] in all_syntax["n_syntax"]:
                    if not topicc.ifTopicAvailable(list[x3+1]):
                        return True, list[x3+1]
                    else:
                        return False, lang.Load_Text("flags", 9)

                # -------------------------------------- #
                # pole
                elif list[x3] in all_syntax["p_syntax"]:
                    if list[x3+1] == "+" or list[x3+1] == "plus" or list[x3+1] == "add":
                        return True, "positive"
                    elif list[x3+1] == "-" or list[x3+1] == "minus" or list[x3+1] == "less":
                        return True, "negative"
                    else:
                        return False, lang.Load_Text("flags", 10)

                # -------------------------------------- #
                # unknown error, should not happen
                else:   ##-## should not happen, is an error
                    return False, lang.Load_Text("flags", 11)

                # end
                # -------------------------------------- #

            else:   # if searched flag not found
                pass

    return False, lang.Load_Text("flags", 12)    # flag is not found



def h_Flag(command):   # help

    for x in all_syntax["h_syntax"]:
        if x in command:
            return True
        else:
            pass



def t_Flag(command):   # topic
    return Flag(command, all_syntax["t_syntax"])



def d_Flag(command):   # date
    success, message = Flag(command, all_syntax["d_syntax"])

    if success == False:   # if no date given
        today = datetime.date.today()  # loads the current date
        message = today.strftime("%Y%m%d")   # use today
        success = True
    else:
        pass

    return success, message



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