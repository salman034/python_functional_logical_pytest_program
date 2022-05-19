def binary_number(number):
    """
    This method is to find binary number
    :param number: int
    :return: binary number
    """
    power_of_two = []
    while number != 1:
        number = int(number / 2)
        power_of_two.append(number)
    return number


def test_binary():
    result = binary_number(100)
    assert result == 1
    print(result)