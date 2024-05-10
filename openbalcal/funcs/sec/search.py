from ..third import flags, config, lang, dategen



def PrintEntrys(topic, date, location, info, value):

    paths = []
    message = []

    # -------------------------------------- #
    # control, what is giving, what is searching
    if not topic == str():   # if not empty
        paths.append("t")

    if not date == str():
        paths.append("d")
        dates = dategen.DateGenerator(date)

    if not location == str():
        if "*" in location:     # wildcard, if you want to search on only your value, or a value what your search include
            paths.append("l*")  # explain below, in search/filter, at location
            location = location.replace("*", "")
        else:
            paths.append("l")

    if not info == str():
        if "*" in info:
            paths.append("i*")
            info = info.replace("*", "")
        else:
            paths.append("i")

    if not value == float():
        paths.append("va")

    # -------------------------------------- #
    # pick the searches lines
    with open(config.ReadConf("paths", "database"), "r") as file:
        for line in file:
            values = line.split(";")

            success = []

            # -------------------------------------- #
            # search/filter
            if "t" in paths:
                if values[0] in topic:
                    success.append(True)
                else:
                    success.append(False)

            if "d" in paths:
                if values[1] in dates:
                    success.append(True)
                else:
                    success.append(False)

            if "l*" in paths:               # some peoples, mabye me itself, write in the location not just one info, more two or three - as example "CologneEst_Edeka"
                if location in values[2]:   # in the search, you can decide to search on a value that's only match with your search, or whether this include
                    success.append(True)    # if we want "only a match equal with the search", we need to look that the line is in your search
                else:                       # the result, my example will only match, if we search after the same "CologneEst_Edeka"
                    success.append(False)   # if we want a search "that your value include", we need to look that your search is in the line
                                            # the result, my example will match both for "Cologne*", "Est*", "Edeka*" or "CologneEst*"
            if "l" in paths:                # for the program, to start the wildcard, include a "*"
                if values[2] in location:
                    success.append(True)
                else:
                    success.append(False)

            if "i*" in paths:
                if info in values[3]:
                    success.append(True)
                else:
                    success.append(False)

            if "i" in paths:
                if values[3] in info:
                    success.append(True)
                else:
                    success.append(False)

            if "va" in paths:
                if float(values[4]) == float(value):
                    success.append(True)
                else:
                    success.append(False)

            # -------------------------------------- #
            # pick the searches lines
            if success.count(False) == 0:  # line is found
                message.append("{}{} {} {} {} {}".format(lang.Load_Text("search", 0), values[0], values[1], values[2], values[3], values[4]))
            else:
                continue
    # end
    # -------------------------------------- #
    return message



def Commandline(command):

    if flags.h_Flag(command):
        print(lang.Load_Text("search", "help"))

    else:

        info = ["placeholder", "placeholder", "placeholder", "placeholder", "placeholder"]
        message = ["placeholder", "placeholder", "placeholder", "placeholder", "placeholder"]

        info[0], message[0] = flags.t_Flag(command)
        info[1], message[1] = flags.d_Flag(command)
        info[2], message[2] = flags.l_Flag(command)
        info[3], message[3] = flags.i_Flag(command)
        info[4], message[4] = flags.va_Flag(command)

        # actually, we cant distinguish between an empty flag and an error, both are errors
        # so actually, both will be replaced with a true and the "wildcard" for everything
        for x in 0, 2, 3:           # for topic, location, and info
            if info[x] == False:    # if flag is missing or an error
                message[x] = str()  # set flag empty
                info[x] = True      # set flag true

        if info[4] == False:        # for value
            message[4] = float()
            info[4] = True

        return PrintEntrys(message[0], message[1], message[2], message[3], message[4])