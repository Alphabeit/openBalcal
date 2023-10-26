# from Functions import Option   # Option fuction, to read the program options
import xml.etree.ElementTree as ET  # xml function


def Load_text(asked_file, text_field):

    # conf_lang = Option.ReadOption("lang")
    conf_lang = "en"

    used_lang_text = ("./Lang/" + conf_lang + ".xml")   # create pfad for text, based on language

    tree = ET.parse(used_lang_text)   # load xml with etree in var
    root = tree.getroot()   # change xml in root_tree, readable for following function

    small_root = root.find(asked_file)   # makes your var smaller, based on the file who asked for the text
    return small_root.find(text_field).text   # filter the searched text_field and return to who asked
