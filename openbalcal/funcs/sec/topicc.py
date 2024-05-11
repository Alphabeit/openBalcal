from ..third import flags, config, lang



def ifTopicAvailable(topic):
    with open(config.ReadConf("paths", "topics"), "r") as file:
        for line in file:
            if topic in line:
                return True
            else:
                continue
        return False



def ReportPole(topic):

    with open(config.ReadConf("paths", "topics"), "r") as file:
        for line in file:
            if topic in line:
                if "positive" in line:
                    return True
                else:
                    return False
            else:
                continue



def ListTopics():

    output = []

    # -------------------------------------- #
    # positive topics
    with open(config.ReadConf("paths", "topics"), "r") as file:

        output.append(lang.Load_Text("topic", 1))

        value = []

        for line in file:
            if "positive" in line:
                topic = line.split(";")
                value.append("| {}".format(topic[0]))
            else:
                continue

        value.sort()
        output.extend(value)

    # -------------------------------------- #
    # negative topics
    with open(config.ReadConf("paths", "topics"), "r") as file:   # need to reopen the file, or the file is already readed

        output.append(lang.Load_Text("topic", 2))

        value = []

        for line in file:
            if "negative" in line:
                topic = line.split(";")
                value.append("| {}".format(topic[0]))
            else:
                continue

        value.sort()
        output.extend(value)

    # end
    # -------------------------------------- #

    return output



def ls_Commandline(command):

    if flags.h_Flag(command):
        print(lang.Load_Text("topic", "help"))

    else:
        return ListTopics()



def CreateTopic(topic, pole):

    if pole == "positive":
        pole = "positive"
    else:
        pole = "negative"

    with open(config.ReadConf("paths", "topics"), "a") as file:
        file.write("{};{};\n".format(topic, pole))



def mk_Commandline(command):

    if flags.h_Flag(command):
        print(lang.Load_Text("topic", "help2"))

    else:

        info = ["placeholder", "placeholder"]
        message = ["placeholder", "placeholder"]

        info[0], message[0] = flags.n_Flag(command)
        info[1], message[1] = flags.p_Flag(command)

        if info.count(False) == 0:   # no errors
            CreateTopic(message[0], message[1])

        else:   # in case of error
            for x in range(0, 2):
                if info[x] is False:
                    return message[x]