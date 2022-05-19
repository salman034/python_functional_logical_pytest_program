def my_factor():
    """
    This function is to find prime factors
    :return: prime factors
    """

    num = int(input())
    while num % 2 == 0:
        print("2")
        num = num / 2

    for i in range(3, int(num / 2), 2):
        while num % i == 0:
            print(i)
            num = num / i
    if num > 1:
        print(num)


if __name__ == "__main__":
    print("Enter any number : ")
    my_factor()