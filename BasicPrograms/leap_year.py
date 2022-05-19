def is_leapyear():
    """
    This function is to find leap year.
    :return: leap year
    """

    if (year > 999) and (year < 10000):
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print("Is leap year")
        else:
            print("It is not a leap year")
    else:
        print("Enter a four digit number")


if __name__ == '__main__':
    print("Enter the year")
    year = int(input())
    is_leapyear()