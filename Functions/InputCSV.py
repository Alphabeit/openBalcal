from Functions.lowerFunctions import Lang, Object, Flags
from Functions import Topic    # to check, if a topic from a new entry available



def Createentry(topic, date, location, info, value):   # Entry, add line

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




def Guided_Mode():

    topic = input(Lang.Load_text("InputCSV.py", "text_1"))   # user guide and input
    date = input(Lang.Load_text("InputCSV.py", "text_2"))
    location = input(Lang.Load_text("InputCSV.py", "text_3"))
    info = input(Lang.Load_text("InputCSV.py", "text_4"))
    value = input(Lang.Load_text("InputCSV.py", "text_5"))

    if not str(date) == "":   # if date is empty, we don't want a d_flag, so that the d_flag returns the date of today
        date = " -d " + str(date)   # so the d_flag is only include, if we have a date

    # okay, why we load the all user-inputs in the commandline?
    # the commandline include ALL return_values and control-mechanics, as example
    #   flag-commands
    #   False control loop
    # if I write all control-mechanics again, this will cost us 10/15 lines codes
    # so, I need only two lines of code (and seven lines of description), to include the same quality for the guided-mode as we have in the commandline
    # the important thing of my code is, to prevent duplicates
    guided_command = "input -t " + topic + str(date) + " -l " + location + " -i " + info + " -va " + str(value)
    Commandline(guided_command)


def Commandline(command):   # a function to read a command, like the tools under linux/unix

    if Flags.h_Flag(command):   # if h_Flag in command, h_flag true
        print(Lang.Load_text("InputCSV.py", "text_6"))   # helppage
        input(Lang.Load_text("Menu.py", "text_2"))   # wait on input

    elif Flags.g_Flag(command):   # if g_Flaf in command, g_Flag true
        Guided_Mode()   # start guided_mode

    else:   # start command

        # the flags of the command, everyone will be run
        topic, t_message = Flags.t_Flag(command)
        date, d_message = Flags.d_Flag(command)
        location, l_message = Flags.l_Flag(command)
        info, i_message = Flags.i_Flag(command)
        value, va_message = Flags.va_Flag(command)

        flag_output = topic + str(date) + location + info + str(value)   # for error control

        if not "False" in flag_output:   # if we have no errors, no False
            Createentry(topic, str(date), location, info, str(value))   # start entry
            print(Lang.Load_text("InputCSV.py", "text_7"))   # Success

        else:
            for message in t_message, d_message, l_message, i_message, va_message:   # in case of error, all error message are in "message"
                if not "Empty" in str(message):   # if we have an error, a False
                    print(message)   # print it
                else:
                    pass