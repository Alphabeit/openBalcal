from Functions import OutputCSV
from Functions.lowerFunctions import Lang, Option, Datevalue



def Switch_Date(date):

    if "today" in date:
        date = Datevalue.Today()
        text_field = "text_1"
        return date, text_field

    elif "yesterday" in date:
        date = Datevalue.Yesterday()
        text_field = "text_2"
        return date, text_field

    elif "this_month" in date:
        date = Datevalue.This_Month()
        text_field = "text_3"
        return date, text_field

    elif "last_month" in date:
        date = Datevalue.Last_Month()
        text_field = "text_4"
        return date, text_field

    elif "this_year" in date:
        date = Datevalue.This_Year()
        text_field = "text_5"
        return date, text_field

    elif "last_year" in date:
        date = Datevalue.Last_Year()
        text_field = "text_6"
        return date, text_field

    else:
        text_field = "text_7"   # Error Message
        return "False", text_field



def Report():

    option = Option.ReadOption("customization", "reports")
    option = option.split(",")    # split the option line in the single reports

    for each in option:   # for each single report

        topic, date = each.split(":")   # split in topic and date

        if topic == "all":   # if we use our wildcard "all" for topic
            topic = ""

        date, text_field = Switch_Date(date)   # deliver the used date and textfield

        if not "False" in str(date):
            report = OutputCSV.Balancerequest(topic, str(date))
            print(Lang.Load_text("Reports.py", text_field) + str(report))

        else:
            print(Lang.Load_text("Reports.py", text_field))

