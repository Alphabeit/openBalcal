from ..third import flags, config, dategen, lang



def Calculation(topic, date):

    total = 0   # var for calculation
    money_mark = config.ReadConf("country", "currency")

    dates = dategen.DateGenerator(date)

    # -------------------------------------- #
    # value picker, all topics
    if topic == str():

        with open(config.ReadConf("paths", "database"), "r") as file:
            for line in file:
                values = line.split(";")

                if values[1] in dates:
                    print(str(values[1] + dates)   ### TEST
                    total += float(values[4])
                else:
                    continue

    # -------------------------------------- #
    # value picker, specific topic
    else:

        with open(config.ReadConf("paths", "database"), "r") as file:
            for line in file:
                values = line.split(";")

                if topic == values[0] and values[1] in dates:
                    total += float(values[4])
                else:
                    continue
    # end
    # -------------------------------------- #

    # the "f" limits the float to two decimal places - mnemonic, f stands for formatting, float and/or fixed point
    return "{} {}".format(f"{total:.2f}", money_mark)



def Commandline(command):

    if flags.h_Flag(command):
        print(lang.Load_Text("output", "help"))

    else:

        info = ["placeholder", "placeholder"]
        message = ["placeholder", "placeholder"]

        info[0], message[0] = flags.t_Flag(command)
        info[1], message[1] = flags.d_Flag(command)

        # -------------------------------------- #
        # topic control - if no topic choose, every topic is meaning
        if info[0] == False:   # if topic is missing
            info[0] = True
            message[0] = str()

        # -------------------------------------- #
        # command control
        if info.count(False) == 0:  # no errors
            return Calculation(message[0], message[1])

        else:  # in case of error
            for x in range(0, 2):
                if info[x] is False:
                    return message[x]
        # end
        # -------------------------------------- #
