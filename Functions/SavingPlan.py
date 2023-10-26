# Saving plan (money)

def Info():
    # Abfrage aus Optionsdatei
    # ist Info Ausgeschaltet?
    # Text aus Optionsdateisdatei

    show_info = True  # Hier die Abfrage rein

    if show_info is True:

        info_text = "Text"  # Hier der Text aus Datei, was beim Plan zu beachten ist
        print(info_text)

        choice_info = input("'Okay' or 'Okay and don't show it again.'? [O / noa]")

        if choice_info == "noa":
            show_info = False
            # Schreib es in Datei
        else:
            continue

    else:  # no showing info any more
        continue


def Created_Plan():

    Info()

    pass


def Output_Rest():
    pass