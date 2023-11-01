from Functions import Lang   # Text, based on language


def ifTopicAvailable(s_topic):   # deliver a True or False value
    with open("./Data/Topics.csv", "r") as csv:
        for line in csv:
            values = line.split(";")   # splits line anlong the ;simicolons;
            topic = values[0]   # writes topic-from-csv in topic-var
            if s_topic == topic:   # checks, if the searched topic the same as the topic from the csv
                return True   # if yes, return True
            else:
                continue   # if not, next line / next topic from csv
        return False   # if every line wrong, return False



def ReportPole(s_topic):   # deliver the pole of the topic
    with open("./Data/Topics.csv", "r") as csv:
        for line in csv:
            values = line.split(";")   # as like as the def_function over this here...
            topic = values[0]
            if s_topic == topic:
                return values[1]   # return "positiv", or "negative"
            else:
                continue



def ls_Commandline(command):   # show which topics are available and if they positiv or negative

    if "-h" in command or "--help" in command or "?" in command:
        print(Lang.Load_text("Topic.py", "text_1"))   # helppage
        input(Lang.Load_text("Topic.py", "text_2"))   # wait on input

    else:   # start command

        def Topic_List(pol):   # the real function - instead to write to code at twice, I created a function to use this twice
            with open("./Data/Topics.csv", "r") as csv:

                if pol == "positiv":   # text, starts to list all topics, based on "pol", positive or negative
                    print(Lang.Load_text("Topic.py", "text_3"))
                else:
                    print(Lang.Load_text("Topic.py", "text_4"))

                for line in csv:
                    pol_Topic = line.split(";")   # line will splited
                    if pol_Topic[1] == pol:   # if pol from topic the same as pol1
                        print("| " + pol_Topic[0])   # print
                    else:   # if not
                        continue   # skip

        Topic_List("positiv")   # first run, first list, positive topics should be showed
        Topic_List("negativ")   # second run, second list, negative topics should be showed



def CreateTopic(topic, pol_symbol):   # create topic

    if pol_symbol == "+":   # if "+" used, we have a positive topic
        pol = "positiv"
    else:   # if "-" used, we have a negative topic
        pol = "negativ"

    with open("./Data/Topics.csv", "a") as csv:   # if the topic is not available yet, and the user used "+" or "-"
        csv.write(str(topic) + ";" + str(pol) + ";")   # writes a new line in the Topic.csv / creates a new topic
        csv.write("\n")



def mk_Guided_Mode():   # create topic
    topic = input(Lang.Load_text("Topic.py", "text_5"))
    pol_symbol = input(Lang.Load_text("Topic.py", "text_6"))

    if pol_symbol == "+" or pol_symbol == "-":   # checks, if the user have you the syntax

        if not ifTopicAvailable(topic):   # checks, if the topic is not available, should prevent duplications
            CreateTopic(topic, pol_symbol)

        else:  # if the topic is all-ready available
            print(Lang.Load_text("Topic.py", "text_7"))

    else:   # if the user didn't use the symbols
        print(Lang.Load_text("Topic.py", "text_8"))



def mk_Commandline(command):

    if "-h" in command or "--help" in command or "?" in command:   # return help
        print(Lang.Load_text("Topic.py", "text_9"))   # helppage
        input(Lang.Load_text("Topic.py", "text_2"))   # wait on input

    elif "-g" in command or "--guided" in command:   # start guided_mode
        mk_Guided_Mode()

    else:   # start command

        paths = list()  # creates list, we need it soon
        given_topic = ""  # create var for topic, empty is also False
        given_pole = ""  # create var for pol, empty is also False

        for path in command.split(" "):  # split the command, so that we can read it
            paths.append(path)

        for x in range(len(paths)):  # for every word from our command

            if paths[x] == "-n" or paths[x] == "--name":  # check, if we have a t-flag
                if not ifTopicAvailable(paths[x+1]):  # check, if topic is not avaliable yet (prevent duplications)
                    given_topic = paths[x+1]
                else:
                    print(Lang.Load_text("Topic.py", "text_7"))
                    break

            elif paths[x] == "-p" or paths[x] == "--pole":  # check, if we have a p-flag
                if paths[x+1] == "+" or paths[x+1] == "-":  # checks, we have a pole in the correct syntax
                    given_pole = paths[x+1]
                else:
                    print(Lang.Load_text("Topic.py", "text_8"))
                    break

            else:
                pass

        if (not given_topic == "" and   # checks, the user have all attributes given
            not given_pole == ""):

            CreateTopic(given_topic, given_pole)   # start entry

        else:
            print(Lang.Load_text("Topic.py", "text_10"))