"""
uri 2533
"""


def sum_grades_times_workloads(gws):
    """
    List (Grade, Workload) -> Number
    """
    return sum(map(lambda gw: gw[0] * gw[1], gws))


def sum_workloads_times_100(gws):
    """
    List (Grade, Workload) -> Number
    """
    return sum(map(lambda gw: gw[1], gws)) * 100


def api(gws):
    """
    List(Grade, Workload) -> Api
    """
    return sum_grades_times_workloads(gws) / sum_workloads_times_100(gws)


def parse_input(string):
    """
    String -> (Grade, Workload)
    """
    grade, workload = [int(gow) for gow in string.split()]
    return grade, workload


def output(result):
    """
    Api -> Message
    """
    return "%.4f" % result


if __name__ == '__main__':
    while True:
        try:
            times = int(input())
            grades_workloads = []
            while times:
                grades_workloads.append(parse_input(input()))
                times -= 1
            print(output(api(grades_workloads)))
        except EOFError:
            break
