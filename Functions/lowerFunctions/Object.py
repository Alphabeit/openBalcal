class Object():   # a fit-object, for a consistent n the whole program

    def __init__(self, Topic, Date, Location, Info, Value):
        self.Topic = str(Topic)   # Topic, the reason why we have pay / get money
        self.Date = int(Date)   # Date, in the syntax JJJJMMTT
        self.Location = str(Location)   # the location, where we have lost or money
        self.Info = str(Info)   # info, like what kind of food or friend is guilt
        self.Value = float(Value)   # the money value

    def asdict(self):   # change the object in a dict, so that's we can search values by key_words
        return {"Topic": str(self.Topic),
                "Date": int(self.Date),
                "Location": str(self.Location),
                "Info": str(self.Info),
                "Value": float(self.Value)
                }


