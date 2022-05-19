import math


def wind_chill(temp, wind_speed):
    """
    This method is to find the wind chill
    :param temp: int
    :param wind_speed: int
    :return: Wind chill
    """
    wind = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * math.pow(wind_speed, 0.16)
    return wind


if __name__ == '__main__':
    temp = int(input("Enter the temprature : "))
    wind_speed = int(input("Enter the wind speed : "))
    print("The Wind Chill is", int(round(wind_chill(temp, wind_speed))))