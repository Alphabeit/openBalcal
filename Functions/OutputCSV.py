from Functions import Object   # class Object, fit-form for entry
from Functions import Lang   # text, based on language
from Functions import Topic    # is used for the topic-based balance calculation
from Functions import Option
import time    # so that output-messages do not disappear immediately



def Blancecalculation(searched_date, month_range, day_range, searched_topic):

    total_balance = 0   # create var for calculation

    with open("./Data/Database.csv", "r") as csv:   # load csv, line for line
        for line in csv:

            values = line.split(";")   # split line in values
            # lode values in Object, so that we can use it as dict
            entry = Object.Object(values[0], values[1], values[2], values[3], values[4])


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
    print(f"{total_balance:.2f}" + " " + money_mark)   # output



def Blancerequest(searched_topic, searched_date):  # function, to start the blance-calculation, responsible for a day-, month-, or a year-based calculation

        if len(searched_date) == 4:  # date-syntax is JJJJ, a year-based calculation
            # balance-starter, syntax is splitet in date, month, day and topic
            # ------------------------------- function ---------------------------------|
            #                | searched date |
            #                |               | range months |
            #                |               |             | range days |
            #                |               |             |            | searched topic |
            Blancecalculation(searched_date, range(1, 13), range(1, 32), searched_topic)
        elif len(searched_date) == 6:   # date-syntax is JJJJMM, a month-based calculation
            Blancecalculation(searched_date, range(0, 1), range(1, 32), searched_topic)
        else:  # date-syntax is JJJJMMDD, a day-based calculation
            Blancecalculation(searched_date, range(0, 1), range(0, 1), searched_topic)



def Guided_Mode():

    print(Lang.Load_text("OutputCSV.py", "text_1"))
    user_searched_topic = input(Lang.Load_text("OutputCSV.py", "text_2"))

    if Topic.ifTopicAvailable(user_searched_topic) or user_searched_topic == "":   # topic must be available or empty

        print(Lang.Load_text("OutputCSV.py", "text_3"))
        print(Lang.Load_text("OutputCSV.py", "text_4"))
        print(Lang.Load_text("OutputCSV.py", "text_5"))
        print(Lang.Load_text("OutputCSV.py", "text_6") + "\n")

        user_searched_date = "FALSE"  # willfully wrong value, var for data input, requirement for first loop
        # as long as length not the same as the length (or length or length) as syntax
        #         |---------------------- JJJJ         |-------------------- JJJJMM         |------------------ JJJJMMTT
        while not len(user_searched_date) == 4 and not len(user_searched_date) == 6 and not len(user_searched_date) == 8:
            user_searched_date = input(Lang.Load_text("OutputCSV.py", "text_7"))  # asks date

        Blancerequest(user_searched_topic, user_searched_date)   # start the calculation

        # sleep for 3 secs, that we can see the print
        time.sleep(3)  # is places on propose under "User"based_Balancerequest, so that the computer can order a request without to need to wait

    else:   # if searched_topic is not available.
        print(Lang.Load_text("OutputCSV.py", "text_8"))



def Commandline(command):   # a function to read a command, like the tools under linux/unix

    if "-h" in command or "--help" in command or "?" in command:   # return help
        print(Lang.Load_text("OutputCSV.py", "text_9"))   # helppage
        input(Lang.Load_text("OutputCSV.py", "text_10"))   # wait on input

    elif "-g" in command or "--guided" in command:   # start guided_mode
        Guided_Mode()

    else:   # start command

        paths = list()   # creates list, we need it soon
        given_topic = ""   # create var for topic, empty is equal no-topic, so if the user didn't give a topic, the var stay empty
        given_date = 11112233   # create var for date, also a value to control, see end of the function

        for path in command.split(" "):   # split the command, so that we can read it
            paths.append(path)

        for x in range(len(paths)):   # for every word from our command

            if paths[x] == "-t" or paths[x] == "--topic":   # check, if we have a topic
                if Topic.ifTopicAvailable(paths[x+1]):   # check, if the topic is really on of our topics
                    given_topic = paths[x+1]
                else:
                    print(Lang.Load_text("OutputCSV.py", "text_8"))
                    break

            elif paths[x] == "-d" or paths[x] == "--date":   # check, if we have a date
                if not paths[x+1] == str:   # checks, is the date truely an integer
                    given_date = paths[x+1]
                else:
                    print(Lang.Load_text("OutputCSV.py", "text_11"))
                    break

            else:
                pass

        if not given_date == 11112233:   # control, that the user have specified a date
            Blancerequest(given_topic, str(given_date))   # start calculation
        else:
            print(Lang.Load_text("OutputCSV.py", "text_12"))