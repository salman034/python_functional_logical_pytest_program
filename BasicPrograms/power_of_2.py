def power_of_2():
    """
    This function is to find power of a given number
    :return: power of 2
    """
    power = 1
    for i in range(1, exponent + 1):
        power = power * number
    print("The power of given number is" ,power)


if __name__ == '__main__':
    number = int(input("Enter the positive integer : "))
    exponent = int(input("enter exponent value : "))
    power_of_2()