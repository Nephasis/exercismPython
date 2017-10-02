from datetime import date
import calendar

def week_day(day):
    days_of_week = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
        }
    return days_of_week[day]

def wdays_in_month(year, month, wday):
    n_days_in_month = calendar.monthrange(year, month)[1]
    days_in_month = [date(year, month, day) for day in range(1, n_days_in_month+1)]
    wday_in_month = [day for day in days_in_month if day.weekday() == week_day(wday)]
    return wday_in_month

def xth_of_month(number):
    mapping = {
        '1st': 0,
        '2nd': 1,
        '3rd': 2,
        '4th': 3,
        '5th': 4,
        'last': -1,
        }
    return mapping[number]


def meetup_day(year, month, wday, number):
    week_days_in_month = wdays_in_month(year, month, wday)

    if number == 'teenth':
        for idx in week_days_in_month:
            if int(idx.day) > 10 and int(idx.day) < 20:
                return idx

    else:
        idx = xth_of_month(number)
        return week_days_in_month[idx]
