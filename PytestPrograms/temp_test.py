def fahrenheit_to_celsius(temperature):
    return temperature - 32 * 5 / 9


def celsius_to_fahrenheit(temperature1):
    return temperature1 * 5 / 9 + 32


def test_fahr_to_cel():
    temp = fahrenheit_to_celsius(45)
    assert temp >= 17.2


def test_cel_to_fahr():
    temp = celsius_to_fahrenheit(35)
    assert temp >= 51.4
