"""
uri 2581

ToorAnswer is "I am Toorg!"
"""


def answer():
    """
    -> ToorgAnswer
    """
    return "I am Toorg!"


if __name__ == '__main__':
    times = int(input())
    while times:
        input()
        print(answer())
        times -= 1
