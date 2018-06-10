"""
uri1010

Id is a integer
repr. the id of a product


Units is a integer
repr. how many units of product


Price is a float
repr. the price of a product


Total is a float
repr. the price times units
"""


def total_price(unit, price):
    """
    Units, Price -> Total
    """
    return unit * price


def parse_input(put):
    """
    String -> Id, Units, Price
    """
    sput = put.split(" ")
    return int(sput[0]), int(sput[1]), float(sput[2])


def output(total):
    """
    Total -> Message
    """
    return "VALOR A PAGAR: R$ %.2f" % total


if __name__ == "__main__":
    _, UNIT_1, PRICE_1 = parse_input(input())
    _, UNIT_2, PRICE_2 = parse_input(input())

    TOTAL_1 = total_price(UNIT_1, PRICE_1)
    TOTAL_2 = total_price(UNIT_2, PRICE_2)

    print(output(TOTAL_1 + TOTAL_2))
