"""
uri 2137


Code is a String 'xxxx' where x[0-9]

Id is a Int


Book is (Code, Id)
"""


def codes_to_books(codes):
    """
    List Code -> List Books
    """
    return list(map(lambda code: (code, int(code)), codes))


def sort_books(books):
    """
    List Book -> List Book
    """
    return sorted(books, key=lambda book: book[1])


def books_to_code(books):
    """
    List Book -> List Code
    """
    return list(map(lambda book: book[0], books))


def output(codes):
    """
    List Code -> Message
    """
    return '\n'.join(codes)


if __name__ == '__main__':
    while True:
        try:
            times = int(input())
            codes = []
            while times:
                codes.append(input())
                times -= 1
            print(output(books_to_code(sort_books(codes_to_books(codes)))))
        except EOFError:
            break
