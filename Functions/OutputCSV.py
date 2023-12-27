from Functions.lowerFunctions import Lang, Object, Option, Flags



def Blancecalculation(searched_date, month_range, day_range, searched_topic):

    total_balance = 0   # create var for calculation

    with open("./Data/Database.csv", "r") as csv:   # load csv, line for line
        for line in csv:

            values = line.split(";")   # split line in values
            # lode values in Object, so that we can use it as dict
            entry = Object.Object(values[0], int(values[1]), values[2], values[3], float(values[4]))


            ### ------------------- month generator ------------------- ###
            for i in month_range:
                if i == 0:   # if month_range is 0, happens when day or month balance is queried
                    new_date = str(searched_date)
                elif len(str(i)) == 1:   # in the months between/include 1 and 9, are just one figure, happens when year balance is queried
                    new_date = str(searched_date) + str("0") + str(i)
                else:   # from the months 10 until 12, are two figure, happens when year balance is queried
                    new_date = str(searched_date) + str(i)


                ### ------------------- day generator ------------------- ###
                for x in day_range:
                    if x == 0:   # if day_range is 0, happens when month or year balance is queried
                        date = str(new_date)
                    elif len(str(x)) == 1:   # in the days between/include 1 and 9, are just one figure, happens when month or year balance is queried
                        date = str(new_date) + str("0") + str(x)
                    else:  # from the days 10 until 31, are two figure, happens when month or year balance is queried
                        date = str(new_date) + str(x)


                    if searched_topic == "":   # if topic is empty, resp. all topics are asked
                        # if date the same as from entry
                        #               | filtered for key "Date" |
                        if int(date) == entry.asdict().get("Date"):
                            # add            |------- Value -----------| to total_balance
                            total_balance += entry.asdict().get("Value")
                        else:   # if date is not the same as entry
                            continue

                    else:  # if we have a calculation based on a topic
                        # if date AND topic the same as from entry - as same a statement higher, just with a filter for topic in addition
                        #                                                                     | filtered for key "Topic" |
                        if int(date) == entry.asdict().get("Date") and str(searched_topic) == entry.asdict().get("Topic"):
                            total_balance += entry.asdict().get("Value")
                        else:   # if date AND topic is not the same as entry
                            continue

    money_mark = Option.ReadOption("customization", "currency")   # return the choices mark from the option.xml file

    # the "f" limits the float to two decimal places - mnemonic, f stands for formatting, float and/or fixed point
    output = f"{total_balance:.2f}" + " " + money_mark
    return output



def Balancerequest(topic, date):  # function, to start the blance-calculation, responsible for a day-, month-, or a year-based calculation

        if len(str(date)) == 4:  # date-syntax is JJJJ, a year-based calculation
            # balance-starter, syntax is splitet in date, month, day and topic
            # -------------------------- function ----------------------------|
            #                | searched date |
            #                |    | range months |
            #                |    |             | range days |
            #                |    |             |            | searched topic |
            return Blancecalculation(date, range(1, 13), range(1, 32), topic)
        elif len(str(date)) == 6:   # date-syntax is JJJJMM, a month-based calculation
            return Blancecalculation(date, range(0, 1), range(1, 32), topic)
        else:  # date-syntax is JJJJMMDD, a day-based calculation
            return Blancecalculation(date, range(0, 1), range(0, 1), topic)



def Guided_Mode():

    topic = input(Lang.Load_text("OutputCSV.py", "text_1"))   # user guide and input
    date = input(Lang.Load_text("OutputCSV.py", "text_2"))

    if not topic == "":   # if topic is empty, we don't want a t_flag, so that the t_flag returns "our wildcard" for all topics
        topic = " -t " + topic   # so the t_flag is only include, if we have a topic

    if not str(date) == "":   # if date is empty, we don't want a d_flag, so that the d_flag returns the date of today
        date = " -d " + str(date)   # so the d_flag is only include, if we have a date

    # see the #comments from "InputCSV.Guided_Mode()"
    guided_command = "output " + topic + date
    Commandline(guided_command)



def Commandline(command):   # a function to read a command, like the tools under linux/unix

    if Flags.h_Flag(command):  # if h_Flag in command, h_flag true
        print(Lang.Load_text("OutputCSV.py", "text_3"))  # helppage
        input(Lang.Load_text("Menu.py", "text_2"))  # wait on input

    elif Flags.g_Flag(command):  # if g_Flaf in command, g_Flag true
        Guided_Mode()  # start guided_mode

    else:  # start command

        # the flags of the command, everyone will be run
        topic, t_message = Flags.t_Flag(command)
        date, d_message = Flags.d_Flag(command)

        if "missing" in topic:   # if we have no topic, then it means all topic, so the var needs to be empty
            topic = ""

        flag_output = topic + str(date)   # for error control

        if not "False" in flag_output:   # if we have no errors, no False
            report = Balancerequest(topic, str(date))
            print(Lang.Load_text("Menu.py", "text_0") + report)  # start output

        else:
            for message in t_message, d_message:  # in case of error, all error message are in "message"
                if not "Empty" in str(message):  # if we have an error, a False
                    print(message)  # print it
                else:
                    pass