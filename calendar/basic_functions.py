def is_leap_year(a):
    if a % 4 == 0 and a % 100 != 0:
        return True
    elif a % 400 == 0:
        return True
    else:
        return False


# to give the total number of days from 1-1-1 at the start of every year
def number_of_days_at_start(year):
    days = 0
    for i in range(1, year + 1):
        if is_leap_year(i):
            days += 366
        else:
            days += 365
    return days


# to give the total number of days at a particular date starting from 1-1-1
def number_of_days(date, month, year):
    days_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    number = number_of_days_at_start(year)
    if is_leap_year(year):
        for i in range(1, month + 1):
            number += days_leap[i]
    else:
        for i in range(1, month):
            number += days[i]
    number += date
    return number


# to give the day at a particular date
def day(date, month, year):
    number = number_of_days(date, month, year)
    value = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
    return value[number % 7]
