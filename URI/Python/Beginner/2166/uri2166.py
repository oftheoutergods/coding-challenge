"""
uri 2166
"""


def sqrt_2_rational(n):
    """
    Number -> Number, Number

    formule to calc the part of sqrt_2 which is rational
    """
    ant = 0
    actual = 1
    while n:
        actual, ant = 2 * actual + ant, actual
        n -= 1
    return ant, actual


def sqrt_2(n):
    """
    Number -> Number
    formule to calc the sqrt of 2
    """
    NUMERATOR, DENOMINATOR = sqrt_2_rational(NUMBER)
    return 1 + (NUMERATOR / DENOMINATOR)


def output(root):
    """
    Number -> Message
    """
    return "%.10f" % root


if __name__ == '__main__':
    NUMBER = int(input())
    print(output(sqrt_2(NUMBER)))
