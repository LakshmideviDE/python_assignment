import calendar
def find_day(date):
    month, day, year = map(int, date.split(' '))
    day_of_the_week = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_of_the_week]
    return day_name.upper()
    
