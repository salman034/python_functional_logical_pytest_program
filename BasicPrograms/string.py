def string_replacement():
    """
    This method responsible for replacement of string.
    :return: String replacement.
    """
    string = 'Hello <<username>>, How are you?'
    print(string.replace("<<username>>", name))


if __name__ == '__main__':
    name = input("Enter your Name : ")
    string_replacement()