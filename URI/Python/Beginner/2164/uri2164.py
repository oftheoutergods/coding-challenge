"""
uri 2164
"""
from math import sqrt


def binet(n):
    """
    Number -> Number

    return n-fibbonacci number
    """
    d = 1 / sqrt(5)
    f = ((1 + sqrt(5)) / 2) ** n
    s = ((1 - sqrt(5)) / 2) ** n
    return d * (f - s)


def output(fib):
    """
    Number -> Message
    """
    return "%.1f" % fib


if __name__ == '__main__':
    NUMBER = int(input())
    print(output(binet(NUMBER)))
