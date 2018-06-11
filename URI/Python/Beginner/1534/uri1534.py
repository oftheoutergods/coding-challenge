"""
uri 1534
"""


def init_matrix(n):
    return ["3" * n for _ in range(0, n)]


def change_diagonal(matrix):
    clone = matrix

    def replace(j, i):
        return j[:i] + "1" + j[i+1:]

    for n, _ in enumerate(matrix):
        clone[n] = replace(clone[n], n)
    return clone


def change_inverse_diagonal(matrix):
    clone = matrix
    size = len(matrix)

    def replace(j, i):
        return j[:size - i - 1] + "2" + j[size - i:]

    for n, _ in enumerate(matrix):
        clone[n] = replace(clone[n], n)
    return clone


def complete_matrix(n):
    return change_inverse_diagonal(change_diagonal(init_matrix(n)))


if __name__ == '__main__':
    while True:
        try:
            matrix = complete_matrix(int(input()))
            for row in matrix:
                print(row)
        except EOFError:
            break
