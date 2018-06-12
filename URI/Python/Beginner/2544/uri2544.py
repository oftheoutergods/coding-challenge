"""
uri 2544
"""
from math import log2


def many_times_used(kage):
    """
    Number -> Number

    how many times the kage bunshin ninjutsu was used
    """
    return log2(kage)


def output(times):
    """
    Number -> Message
    """
    return "%i" % times


if __name__ == '__main__':
    while True:
        try:
            bunshins = int(input())
            print(output(many_times_used(bunshins)))

        except EOFError:
            break
