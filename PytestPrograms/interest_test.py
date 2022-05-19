def math_power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result


def calculate_interest(year, principle, rate):
    r = rate / (12 * 100)
    months = (12 * year)
    return (principle * r) / 1 - math_power((1 + r), months)


def test():
    result = calculate_interest(4, 100000, 7)
    assert result >= 98.18
    print("interest rate: ", result)
