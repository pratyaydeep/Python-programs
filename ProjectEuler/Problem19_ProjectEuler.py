# Ham kiem tra nam nhuan
def leap_year(n):
    if n % 4 == 0:
        if n % 100 != 0:
            return True
        else:
            if n % 400 == 0:
                return True
            else:
                return False
    else:
        return False

# Xac dinh thu cua ngay 1 Jan 1901
# 1 Jan 1900 la Monday
week_day = {
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "3": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday"
}

months ={
    "January": 0,
    "February": 31,
    "March": 59,
    "April": 90,
    "May": 120,
    "June": 151,
    "July": 181,
    "August": 212,
    "September": 243,
    "October": 273,
    "November": 304,
    "December": 334
}

check_month = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

# Ham kiem tra thu
def check_day1(n):
    a = n % 7
    return week_day[str(a)]

# Ham tinh so ngay den dau nam ke tu 1 Jan 1900
def days(year):
    bonus = 0
    number = 0
    if year == 1900:
        return 0
    else:
        for i in range(1900,year):
            if leap_year(i):
                bonus += 1
            number += 365
        number += bonus
        return number

# Ham kiem tra ngay dau thang la thu may
def check_day2(month,year):
    total = days(year)
    total += months[check_month[str(month)]]
    if leap_year(year) and month >=3:
        total += 1
    return check_day1(total)

# Ham tinh so ngay chu nhat la dau thang
def count_sunday(year):
    result = 0
    for i in range(1900,year):
        for j in range(1,13):
            if check_day2(j,i) == "Sunday":
                result += 1
    return result

sundays_1900 = count_sunday(1901)
sundays_2000 = count_sunday(2001)
print (sundays_1900)
print (sundays_2000)
# Vi ngay 1 Jan 1901 la Tuesday nen ok
print (sundays_2000-sundays_1900)