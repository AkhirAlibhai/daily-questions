import datetime


def working_days(year, days_off, holidays):
    my_return = []

    curr_date = datetime.datetime(year, 1, 1)
    while curr_date.year == year:
        # To make the python weekday to be the same as the input
        # To check if the day is a holiday
        if curr_date.isoweekday() % 7 not in days_off and curr_date.strftime("%Y-%m-%d") not in holidays:
            my_return.append(curr_date.strftime("%Y-%m-%d"))

        curr_date += datetime.timedelta(days=1)

    return my_return
