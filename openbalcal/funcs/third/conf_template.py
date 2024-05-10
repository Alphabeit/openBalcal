def Version():
    return "v0.3.0"



def Template():
    template = ('''version: v0.3.0
config:
  paths:
    database: /etc/openbalcal/database.csv
    topics: /etc/openbalcal/topics.csv
    
  country:
    currency: DOLLAR
    lang: /bin/openbalcal/lang/en_US.yml
  
  funcs:
    report: all:today,all:this_month''')

    return template
