from datetime import date, datetime, timedelta
import calendar


def get_date(day):
    if day:
        year, month = (int(x) for x in day.split('-'))
        return date(year, month, day=1)
    return datetime.now()


def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
