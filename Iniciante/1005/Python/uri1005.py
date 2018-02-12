'''
uri 1005
'''

def average(first_number: float, second_number: float) -> float:
    '''
    determines the average with five decimal places of precision, given two numbers.
    '''
    value = (first_number*3.5 + second_number*7.5)/11
    return round(value, 5)


def presentation(number):
    '''
    presents a number with five decimal places of precision, given a number
    '''
    return "MEDIA = %.5f" % number



if __name__ == "__main__":
    NUMBER1 = float(input())
    NUMBER2 = float(input())

    RESULT = average(NUMBER1, NUMBER2)

    print(presentation(RESULT), end='\n')
