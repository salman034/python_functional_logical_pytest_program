def week_test(year, month, day):
    """
    This method is to find day in the given year
    :param year: int
    :param month: int
    :param day: int
    :return: day
    """
    day_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    year = year - (2 * 7 - month) / 12
    x = year + year/4 - year/100 + year/400
    month = month + 12 * ((2 * 7 - month) / 12) - 2
    day = int(day + x + 31 * month / 12) % 7
    return day_list[day]


def test_calculate():
    result = week_test(2022, 3, 11)
    assert result == "friday"
    print(result)
