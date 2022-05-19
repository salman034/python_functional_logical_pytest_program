import math


def distance(x, y):
    """
    This method is to find euclidean distance of two points
    :param x: int
    :param y: int
    :return: Euclidean distance
    """
    p1 = [0, 0]
    p2 = [x, y]
    euclidean_distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print(euclidean_distance)


if __name__ == '__main__':
    distance(2, 5)