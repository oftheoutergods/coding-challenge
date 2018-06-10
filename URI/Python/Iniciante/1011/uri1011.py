"""
uri1011

Radius is a float
repr. the radius of a Sphere


Volume is a float
repr. the volume of a Sphere
"""


PI = 3.14159


def parse_input(put):
    """
    String -> Radius
    """
    return float(put)


def volume_sphere(radius):
    """
    Radius -> Volume
    """
    return (4 / 3) * PI * radius ** 3


def output(volume):
    """
    Volume -> Message
    """
    return "VOLUME = %.3f" % volume


if __name__ == "__main__":
    RADIUS = parse_input(input())
    VOLUME = volume_sphere(RADIUS)

    print(output(VOLUME))
