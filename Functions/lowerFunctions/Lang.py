from Functions.lowerFunctions import Option
import xml.etree.ElementTree as ET  # xml function


def Load_text(asked_file, text_field):

    conf_lang = Option.ReadOption("customization", "lang")  # the selected language

    used_lang_file = ("./Lang/" + conf_lang + ".xml")   # create pfad for text, based on language

    tree = ET.parse(used_lang_file)   # load xml with etree in var
    root = tree.getroot()   # change xml in root_tree, readable for following function

    small_root = root.find(asked_file)   # makes your var smaller, based on the file who asked for the text

    if not "text_0" in text_field:   # if a normal text_field asked
        text_line = (small_root.find("text_0").text + small_root.find(text_field).text)   # filter the searched text_field and create a text_line
        return text_line   # return the text_line

    else:   # if the text_field 0 asked
        text_line = (small_root.find("text_0").text)  # filter the searched text_field and create a text_line
        return text_line  # return the text_line