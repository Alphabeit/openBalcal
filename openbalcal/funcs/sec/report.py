from ..sec import output
from ..third import config, lang, dategen
import re



def FirstMessage():

    message = []   # var for message

    configuration = config.ReadConf("funcs", "report").split(",")

    for each in configuration:
        topic, period = each.split(":")

        if topic == "all":
            topic = str()

        nr_alias, period = dategen.DateAliasSwitch(period)

        text_field = nr_alias

        if re.findall("[1-6]", str(nr_alias)):
            info = True
        else:
            info = False

        text = lang.Load_Text("report", text_field)

        if not info == False:
            total = output.Calculation(topic, period)
            message.append("{}{}".format(text, total))

        else:
            message.append(text)

    return message