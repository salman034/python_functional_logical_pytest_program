def harmonic_value():
    """
    This function is to find Harmonic number of a given number.
    :return: harmonic number
    """

    sum = 0
    for i in range(1, harmonic_number + 1):
        sum = sum + 1 / i
    print(sum)


if __name__ == '__main__':
    print("Enter the value of n")
    harmonic_number = int(input())
    harmonic_value()