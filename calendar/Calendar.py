import basic_functions as bs


def print_month(month, year):
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}
    print("Month: ", months[month])
    days_ = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 0}
    print("Su  Mo  Tu  We  Th  Fr  Sa")
    parts_to_skip = days_[bs.day(1, month, year)]
    days_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    date = {1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "10", 11: "11",
            12: "12", 13: "13", 14: "14", 15: "15", 16: "16", 17: "17", 18: "18", 19: "19", 20: "20", 21: "21",
            22: "22", 23: "23", 24: "24", 25: "25", 26: "26", 27: "27", 28: "28", 29: "29", 30: "30", 31: "31"}
    if bs.is_leap_year(year):
        count = parts_to_skip
        for i in range(0, parts_to_skip):
            print("  ", end="  ")
        for i in range(1, days_leap[month]):
            if (count + 1) % 7 == 0:
                print(date[i])
            else:
                print(date[i], end="  ")
            count += 1
    else:
        count = parts_to_skip
        for i in range(0, parts_to_skip):
            print("  ", end="  ")
        for i in range(1, days[month] + 1):
            if (count + 1) % 7 == 0:
                print(date[i])
            else:
                print(date[i], end="  ")
            count += 1
    print()
    print()


def print_year(year):
    print()
    print("Year:", year)
    print()
    for i in range(1, 13):
        print_month(i, year)


while True:
    value = input("Press 1 for printing an year and 2 for printing month: ")
    if value == "1":
        y = input("Enter the year: ")
        print_year(int(y))
        break
    elif value == "2":
        try:
            y = int(input("Enter the year: "))
        except ValueError:
            print("Enter a valid value next time")
            continue
        if y <= 0:
            print("Enter a valid value next time")
            continue
        try:
            m = int(input("Enter the month: "))
        except ValueError:
            print("Enter a valid value next time")
            continue
        if 0 >= m >= 13:
            print("Enter a valid value next time")
            continue
        print_month(m, y)
        break
    else:
        print("Enter a valid value next time")
