from ..third import config
import yaml



def Load_Text(script, field):

    lang_path = config.ReadConf("country", "lang")

    with open(lang_path, "r") as file:
        text_file = yaml.safe_load(file)

    if field == 0:
        text_box = (text_file["file"][script][0])
        return text_box

    else:
        text_box = (text_file["file"][script][0] + text_file["file"][script][field])
        return text_box