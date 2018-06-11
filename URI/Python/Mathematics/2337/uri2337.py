"""
uri 2337
"""
from math import sqrt
from fractions import Fraction


def binet(n):
    """
    Number -> Number

    return n-fibbonacci number
    """
    d = 1 / sqrt(5)
    f = ((1 + sqrt(5)) / 2) ** n
    s = ((1 - sqrt(5)) / 2) ** n
    return int(d * (f - s))


def prob(n):
    """
    Number -> Fraction
    """
    return Fraction(binet(n) + binet(n + 1), 2 ** (n))


def output(frac):
    """
    Fraction -> Message
    """
    return "%i/%i" % (frac.numerator, frac.denominator)


if __name__ == '__main__':
    while True:
        try:
            case = int(input())
            print(output(prob(case)))
        except EOFError:
            break
