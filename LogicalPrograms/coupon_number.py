import random


def coupon_number():
    codeset = set()

    while len(codeset) < code_count:
        code = (str(random.randint(100000, 999999)))
        codeset.add(code)

    return codeset


if __name__ == '__main__':
    code_count = int(input("Enter the code : "))
    print(coupon_number())