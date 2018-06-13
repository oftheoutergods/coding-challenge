"""
uri 2547

Min is a int
repr. the min of a interval

Max is a int
repr. the max of a interval
"""


def interval(n_min, n_max):
    """
    Min, Max-> (List Number -> List Number)
    """
    def _interval(l):
        return list(filter(lambda n: n >= n_min and n <= n_max, l))
    return _interval


def parse_input(string):
    """
    String -> [Number, Min, Max]
    """
    return [int(s) for s in string.split()]


if __name__ == '__main__':
    while True:
        try:
            times, n_min, n_max = parse_input(input())
            numbers = []
            n_interval = interval(n_min, n_max)
            while times:
                numbers.append(int(input()))
                times -= 1
            print(len(n_interval(numbers)))
        except EOFError:
            break
