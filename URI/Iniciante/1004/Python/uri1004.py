'''
uri 1004
'''

def prod_two_numbers(first_number: int, second_number: int) -> int:
    '''
    computes the prod of two numbers, given the two numbers
    '''
    return first_number * second_number


def presentation(number: int) -> str:
    '''
    presents a number, given the number
    '''
    return "PROD = %i" % number


if __name__ == "__main__":
    NUMBER1 = int(input())
    NUMBER2 = int(input())

    RESULT = prod_two_numbers(NUMBER1, NUMBER2)

    print(presentation(RESULT), end='\n')
