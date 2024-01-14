def check_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 4 == 0 and year % 400 == 0:
        return 1
    else:
        return 0

year = int(input())

print(check_leap_year(year))