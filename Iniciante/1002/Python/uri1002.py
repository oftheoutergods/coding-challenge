'''
uri 1002
'''

def pi() -> float:
    '''
    value of pi
    '''
    return 3.14159


def circle_area(radius: float) -> float:
    '''
    determines the area of circle, given the radius
    '''
    area = pi() * radius**2
    return round(area, 4)


def presentation(c_area: float) -> str:
    '''
    presents the area of circle
    '''
    return "A=%.4f" % c_area


if __name__ == "__main__":
    RADIUS = float(input())

    RESULT = circle_area(RADIUS)

    print(presentation(RESULT), end='\n')
