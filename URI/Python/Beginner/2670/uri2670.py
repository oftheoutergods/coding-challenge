
'''
Mult is a element of Mults

People is a Int

Minutes is a Int
'''

MULTS = [(0, 2, 4), (4, 2, 0), (2, 0, 2)]


def mult_people(mult, people):
    """
    Mult, People -> Minutes
    """
    return mult[0] * people[0] + mult[1] * people[1] + mult[2] * people[2]


def best_minutes(pleople):
    """
    Pleople -> Minutes
    """
    return min(list(map(lambda m: mult_people(m, pleople), MULTS)))


if __name__ == "__main__":
    PLEOPLE = [int(p) for p in [input(), input(), input()]]
    print(best_minutes(PLEOPLE))
