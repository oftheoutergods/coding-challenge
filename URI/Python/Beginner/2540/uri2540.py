"""
uri 2540

Vote is a enum
  - 1
  - 0
repr. the votes(1-must, 0-not must) of a poll


Result is a Bool
repr. the result of a poll, True if 2/3 of votes is Vote must
"""


def parse_input(string):
    """
    String -> List Vote
    """
    return [int(vote) for vote in string.split()]


def result_poll(votes):
    """
    List Votes -> Result
    """
    return sum(votes) >= 2 / 3 * len(votes)


def output(result):
    """
    Result -> Message
    """
    return "impeachment" if result else "acusacao arquivada"


if __name__ == '__main__':
    while True:
        try:
            many_votes = int(input())
            print(output(result_poll(parse_input(input()))))

        except EOFError:
            break
