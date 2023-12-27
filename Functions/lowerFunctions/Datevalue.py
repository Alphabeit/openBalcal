# This script holds all function that return a date.
# We can deliver the date of a day, month or year - at our currently or the last position.

from datetime import date, timedelta



def Today():

    today = date.today()   # loads the currently date
    return int(today.strftime("%Y%m%d"))   # change the date in syntax that work with the syntax



def Yesterday():

    yesterday = date.today() - timedelta(days = 1)   # go in the past a day back, yesterday
    return (yesterday.strftime("%Y%m%d"))



def This_Month():

    today = date.today()
    return (today.strftime("%Y%m"))



def Last_Month():

    last_month = date.today().replace(day=1) - timedelta(days=1)   # loads the first of the month and go then a day back in the past
    return int(last_month.strftime("%Y%m"))



def This_Year():

    today = date.today()
    return int(today.strftime("%Y"))



def Last_Year():

    today = date.today()
    year = today.strftime("%Y")
    year = int(year) - 1
    return int(year)