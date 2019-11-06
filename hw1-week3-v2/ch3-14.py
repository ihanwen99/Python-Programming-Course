def isLeapyear():
    year = input("Please input the year you want to check: ")
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print year, "is leap year."
    else:
        print year, "is not leap year."


if __name__ == '__main__':
    isLeapyear()
