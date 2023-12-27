from Functions.lowerFunctions import Lang, Flags


def ifTopicAvailable(s_topic):   # deliver a True or False value
    with open("./Data/Topics.csv", "r") as csv:
        for line in csv:
            values = line.split(";")   # splits line along the ;semicolons;
            topic = values[0]   # writes topic-from-csv in topic-var
            if s_topic == topic:   # checks, if the searched topic the same as the topic from the csv
                return True   # if yes, return True
            else:
                continue   # if not, next line / next topic from csv
        return False   # if every line wrong, return False



def ReportPole(s_topic):   # deliver the pole of the topic / is for the script, not the user / to find under "InputCSV.py"
    with open("./Data/Topics.csv", "r") as csv:
        for line in csv:
            values = line.split(";")   # as like as the def_function over this here...
            topic = values[0]
            if s_topic == topic:
                return values[1]   # return "positiv", or "negative"
            else:
                continue



def ls_Commandline(command):   # show which topics are available and if they positiv or negative

    if Flags.h_Flag(command):   # if h_Flag in command, h_flag true
        print(Lang.Load_text("Topic.py", "text_1"))   # helppage
        input(Lang.Load_text("Menu.py", "text_2"))   # wait on input

    else:   # start command

        def ls_TopicList(pol):   # the real function - instead to write to code at twice, I created a function to use this twice
            with open("./Data/Topics.csv", "r") as csv:

                if pol == "positiv":   # text, starts to list all topics, based on "pol", positive or negative
                    print(Lang.Load_text("Topic.py", "text_2"))
                else:
                    print(Lang.Load_text("Topic.py", "text_3"))

                for line in csv:
                    pol_Topic = line.split(";")   # line will splited
                    if pol_Topic[1] == pol:   # if pol from topic the same as pol1
                        print("| " + pol_Topic[0])   # print
                    else:   # if not
                        continue   # skip

        ls_TopicList("positiv")   # first run, first list, positive topics should be showed
        ls_TopicList("negativ")   # second run, second list, negative topics should be showed



def mk_CreateTopic(topic, pol_symbol):   # create topic

    if pol_symbol == "positiv":   # if "+" used, we have a positive topic
        pol = "positiv"
    else:   # if "-" used, we have a negative topic
        pol = "negativ"

    with open("./Data/Topics.csv", "a") as csv:   # if the topic is not available yet, and the user used "+" or "-"
        csv.write(str(topic) + ";" + str(pol) + ";")   # writes a new line in the Topic.csv / creates a new topic
        csv.write("\n")



def mk_Guided_Mode():   # create topic
    name = input(Lang.Load_text("Topic.py", "text_4"))
    pole = input(Lang.Load_text("Topic.py", "text_5"))

    # see the #comments from "InputCSV.Guided_Mode()"
    guided_command = "mktopic -n " + name + " -p " + pole
    mk_Commandline(guided_command)



def mk_Commandline(command):

    if Flags.h_Flag(command):  # if h_Flag in command, h_flag true
        print(Lang.Load_text("Topic.py", "text_6"))  # helppage
        input(Lang.Load_text("Menu.py", "text_2"))  # wait on input

    elif Flags.g_Flag(command):  # if g_Flag in command, g_Flag true
        mk_Guided_Mode()  # start guided_mode

    else:  # start command

        # the flags of the command, everyone will be run
        name, n_message = Flags.n_Flag(command)
        pole, p_message = Flags.p_Flag(command)

        flag_output = name + pole  # for error control

        if not "False" in flag_output:  # if we have no errors, no Falses
            mk_CreateTopic(name, pole)  # start output
            print(Lang.Load_text("InputCSV.py", "text_7"))

        else:
            for message in n_message, p_message:  # in case of error, all error message are in "message"
                if not "Empty" in str(message):  # if we have an error, a False
                    print(message)  # print it
                else:
                    pass