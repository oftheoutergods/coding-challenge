"""
uri 2582

Button is a int[0-10]

Song is a element of SONGS
"""

SONGS = [
    "PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!",
    "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"]


def parse_input(string):
    """
    String -> List Number
    """
    return [int(number) for number in string.split()]


def position(numbers):
    """
    List Number -> Button
    """
    return sum(numbers)


def song_choosed(button):
    """
    Button -> Song
    """
    return SONGS[button]


if __name__ == '__main__':
    times = int(input())
    while times:
        print(song_choosed(position(parse_input(input()))))
        times -= 1
