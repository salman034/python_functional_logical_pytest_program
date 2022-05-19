def sum_of_three():
    """
    This method is to find sum of three integers
    :return: sum of three integers
    """

    array = [0 for index in range(number_of_elements)]
    for index in range(number_of_elements):
        array[index] = int(input('Enter element : '))
    print(array)

    for i in range(number_of_elements):
        j = i + 1
        for j in range(j, number_of_elements):
            k = j + 1
            for k in range(k, number_of_elements):
                if array[i] + array[j] + array[k] == 0:
                    print(array[i], array[j], array[k])


if __name__ == '__main__':
    number_of_elements = int(input('Enter number of elements : '))
    sum_of_three()