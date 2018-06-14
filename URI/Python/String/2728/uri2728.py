"""
uri 2728

Extreme is (String, String)
repr. the first and the last letter in a word
"""
from functools import reduce


COBOL = ['cobol', 'COBOL']


def parse_input(string):
    """
    String -> List Extreme
    """
    return list(map(lambda word: (word[:1], word[-1:]), string.split('-')))


def cobol(extremes):
    """
    List Extreme -> Bool
    """
    def check(n):
        return COBOL[0][n] in extremes[n] or COBOL[1][n] in extremes[n]

    return reduce(bool.__and__, map(check, list(range(0, 5))))


def output(result):
    """
    Bool -> Message
    """
    return "GRACE HOPPER" if result else "BUG"


if __name__ == '__main__':
    while True:
        try:
            print(output(cobol(parse_input(input()))))
        except EOFError:
            break
