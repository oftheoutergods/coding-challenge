"""
uri 1555

Winner is a enum
  - "Rafael"
  - "Carlos"
  - "Beto"
repr. the name of winner
"""


def rafael_fun(x, y):
    """
    Number, Number -> Number
    """
    return (3 * x) ** 2 + y ** 2


def beto_fun(x, y):
    """
    Number, Number -> Number
    """
    return 2 * (x ** 2) + (5 * y) ** 2


def carlos_fun(x, y):
    """
    Number, Number -> Number
    """
    return -100 * x + y ** 3


def winner(x, y):
    """
    Number, Number -> Winner
    """
    rafael, beto, carlos = rafael_fun(x, y), beto_fun(x, y), carlos_fun(x, y)
    if rafael >= beto and rafael >= carlos:
        return "Rafael"
    if beto >= carlos:
        return "Beto"
    return "Carlos"


def parse_input(put):
    """
    String -> [Int, Int]
    """
    return map(lambda i: int(i), put.split())


def output(winner):
    """
    Winner -> Message
    """
    return "%s ganhou" % winner


if __name__ == "__main__":
    times = int(input())

    while times > 0:
        print(output(winner(*parse_input(input()))))
        times -= 1
