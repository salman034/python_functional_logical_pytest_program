def quadratic_equation():
    """
    This methed is to find out Quadratic equation.
    :return: quadratic equation
    """
    delta = coefficient_b * coefficient_b - 4 * coefficient_a * constant
    if delta < 0:
        print('Root not possible')
    else:
        root1 = -1 * coefficient_b - (delta / (2 * coefficient_a)) ** 0.5
        root2 = -1 * coefficient_b + (delta / (2 * coefficient_a)) ** 0.5
        print('Root 1 : %.2f' % (root1), 'Root 2 : %.2f' % (root2))


if __name__ == '__main__':
    coefficient_a = int(input('Enter coefficient of x^2 : '))
    coefficient_b = int(input('Enter coefficient of x : '))
    constant = int(input('Enter constant value : '))
    quadratic_equation()