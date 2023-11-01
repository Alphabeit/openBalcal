import xml.etree.ElementTree as ET      # xml function



def ReadOption(ask_option_grp, ask_option):

    tree = ET.parse("./Option.xml")  # load xml with etree in var
    root = tree.getroot()  # change xml in root_tree, readable for following function

    small_root = root.find(ask_option_grp)  # makes your var smaller, based on the file who asked for the text

    text = (small_root.find(ask_option).text)  # filter the searched text_field and create a text_string
    return text  # return the text_string