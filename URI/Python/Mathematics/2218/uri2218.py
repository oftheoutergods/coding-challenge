"""
uri 2218

Concrete mathematics knuth
"""


def number_planes(n):
    """
    Number -> Number
    """
    return (n ** 2 + n + 2) // 2


if __name__ == '__main__':
    times = int(input())

    while times > 0:
        print(number_planes(int(input())))
        times -= 1
