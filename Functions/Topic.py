from Functions import Lang   # Text, based on language



def Report_Topics():   # show which topics are available and if they positiv or negative

    def Topic_List(pol):   # the real function - instead to write to code at twice, I created a function to use this twice
        with open("./Data/Topics.csv", "r") as csv:

            if pol == "positiv":   # text, starts to list all topics, based on "pol", positive or negative
                print(Lang.Load_text("Topic.py", "text_1"))
            else:
                print(Lang.Load_text("Topic.py", "text_2"))

            for line in csv:
                pol_Topic = line.split(";")   # line will splited
                if pol_Topic[1] == pol:   # if pol from topic the same as pol1
                    print("| " + pol_Topic[0])   # print
                else:   # if not
                    continue   # skip

    Topic_List("positiv")   # first run, first list, positive topics should be showed
    Topic_List("negativ")   # second run, second list, negative topics should be showed



def ifTopicAvailable(s_topic):
    with open("./Data/Topics.csv", "r") as csv:
        for line in csv:
            werte = line.split(";")   # splits line anlong the ;simicolons;
            topic = werte[0]   # writes topic-from-csv in topic-var
            if s_topic == topic:   # checks, if the searched topic the same as the topic from the csv
                return True   # if yes, return True
            else:
                continue   # if not, next line / next topic from csv
        return False   # if every line wrong, return False



def Ausgabe_Polung_Topic(s_topic):              # welche Polung der Topic hat und Übergabe des entsprechenden Wertes
                                                # Ausgabe für Programm
    pass



def new_Topic():
    topic = input(Lang.Load_text("Topic.py", "text_3"))
    pol_symbol = input(Lang.Load_text("Topic.py", "text_4"))

    if not ifTopicAvailable(topic):   # checks, if the topic is not available, should prevent duplications

        if pol_symbol == "+" or pol_symbol == "-":    # checks, if the syntax (+ or -) is used
            if pol_symbol == "+":   # if "+" used, we have a positive topic
                pol = "positiv"
            else:   # if "-" used, we have a negative topic
                pol = "negativ"

            with open("./Data/Topics.csv", "a") as csv:   # if the topic is not available yet, and the user used "+" or "-"
                csv.write(str(topic) + ";" + str(pol) + ";")   # writes a new line in the Topic.csv / creates a new topic
                csv.write("\n")

        else:   # if the user didn't use the symbols
            print(Lang.Load_text("Topic.py", "text_5"))

    else:   # if the topic is all-ready available
        print(Lang.Load_text("Topic.py", "text_6"))
