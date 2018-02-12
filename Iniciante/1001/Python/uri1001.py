'''
uri 1001
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
    return "X = %i" % number


if __name__ == "__main__":
    number1 = int(input())
    number2 = int(input())

    result = sum_two_numbers(number1, number2)

    print(presentation(result), end='\n')
