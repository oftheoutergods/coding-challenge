'''
uri 1003
'''

def sum_two_numbers(first_number: int, second_number: int) -> int:
    '''
    computes the sum of two numbers, given the two numbers
    '''
    return first_number + second_number


def presentation(number: int) -> str:
    '''
    presents a number, given the number
    '''
    return "SOMA = %i" % number


if __name__ == "__main__":
    NUMBER1 = int(input())
    NUMBER2 = int(input())

    RESULT = sum_two_numbers(NUMBER1, NUMBER2)

    print(presentation(RESULT), end='\n')
