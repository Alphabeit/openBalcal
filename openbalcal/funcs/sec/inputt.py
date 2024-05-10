from ..sec import topicc
from ..third import flags, config, lang



def Createentry(topic, date, location, info, value):

    if topicc.ReportPole(topic) is True:   # if topic positive
        pass
    else:
        value = "-{}".format(value)

    with open(config.ReadConf("paths", "database"), "a") as file:
        file.write("{};{};{};{};{};\n".format(topic, date, location, info, value))



def Commandline(command):

    if flags.h_Flag(command):
        print(lang.Load_Text("inputt", "help"))

    else:

        info = ["placeholder", "placeholder", "placeholder", "placeholder", "placeholder"]
        message = ["placeholder", "placeholder", "placeholder", "placeholder", "placeholder"]

        info[0], message[0] = flags.t_Flag(command)
        info[1], message[1] = flags.d_Flag(command)
        info[2], message[2] = flags.l_Flag(command)
        info[3], message[3] = flags.i_Flag(command)
        info[4], message[4] = flags.va_Flag(command)

        if info.count(False) == 0:   # no errors
            Createentry(message[0], message[1], message[2], message[3], message[4])

        else:   # in case of error
            for x in range(0, 5):
                if info[x] is False:
                    return message[x]