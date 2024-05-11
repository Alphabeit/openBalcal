from datetime import date, timedelta



def DateGenerator(date):

    dates = []

    # -------------------------------------- #
    # date generator - in case of year
    if len(str(date)) == 4:

        for x in range(1, 13):
            for y in range(1, 32):

                if len(str(x)) == 1:
                    x = "0{}".format(x)
                if len(str(y)) == 1:
                    y = "0{}".format(y)

                dates.append("{}{}{}".format(date, x, y))

    # -------------------------------------- #
    # date generator - in case of month
    elif len(str(date)) == 6:

        for y in range(0, 32):
            if len(str(y)) == 1:
                y = "0{}".format(y)

            dates.append("{}{}".format(date, y))

    # -------------------------------------- #
    # date generator - in case of day
    else:  # len of date is 8
        dates.append("{}".format(date))

    # end
    # -------------------------------------- #
    
    return dates



def DateAliasSwitch(datetxt):
    if "today" in str(datetxt):
        today = date.today()  # loads the current date
        return 1, today.strftime("%Y%m%d")  # change the date in correct syntax

    elif "yesterday" in str(datetxt):
        yesterday = date.today() - timedelta(days=1)
        return 2, yesterday.strftime("%Y%m%d")

    elif "this" in str(datetxt) and "month" in str(datetxt):
        today = date.today()
        return 3, today.strftime("%Y%m")

    elif "this" in str(datetxt) and "year" in str(datetxt):
        today = date.today()
        return 4, today.strftime("%Y")

    elif "last" in str(datetxt) and "month" in str(datetxt):
        last_month = date.today().replace(day=1) - timedelta(days=1)
        return 5, last_month.strftime("%Y%m")

    elif "last" in str(datetxt) and "year" in str(datetxt):
        today = date.today()
        year = today.strftime("%Y")
        year = int(year) - 1
        return 6, year

    else:
        return 7, "0"   # Err
