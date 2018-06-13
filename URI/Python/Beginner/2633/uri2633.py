'''
Product is (Name, Price)


Price is a Int


Name is a String
'''


def parse_input(string):
    """
    String -> Product
    """
    name, price = string.split()
    return name, int(price)


def sort_products(products):
    """
    List Product-> List Product
    """
    return sorted(products, key=lambda x: x[1])


def products_names(products):
    """
    List Product -> List Name
    """
    return list(map(lambda product: product[0], products))


def output(names):
    """
    List Name -> String
    """
    return ' '.join(names)


if __name__ == "__main__":
    while True:
        try:
            times = int(input())
            products = []
            while times:
                products.append(parse_input(input()))
                times -= 1
            print(output(products_names(sort_products(products))))
        except EOFError:
            break
