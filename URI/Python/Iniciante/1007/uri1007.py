'''
uri 1007
'''

def difference(first: int, second: int, third: int, fourth: int) -> int:
    '''
    determines the difference between the product f s and the product t fo, given the numbers
    '''
    return first*second - third*fourth


def presentation(number: int) -> str:
    '''
    presents a integer number, given the number
    '''
    return "DIFERENCA = %i" % number


if __name__ == "__main__":
    NUMBER1 = int(input())
    NUMBER2 = int(input())
    NUMBER3 = int(input())
    NUMBER4 = int(input())

    RESULT = difference(NUMBER1, NUMBER2, NUMBER3, NUMBER4)

    print(presentation(RESULT), end='\n')
