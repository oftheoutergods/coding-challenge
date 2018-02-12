'''
uri 1006
'''

def average(first_number: float, second_number: float, third_number: float) -> float:
    '''
    determines the average with one decimal place of precision, given three numbers.
    '''
    value = (first_number*2 + second_number*3 + third_number*5)/10
    return round(value, 1)


def presentation(number):
    '''
    presents a number with one decimal place of precision, given a number
    '''
    return "MEDIA = %.1f" % number



if __name__ == "__main__":
    NUMBER1 = float(input())
    NUMBER2 = float(input())
    NUMBER3 = float(input())
    
    RESULT = average(NUMBER1, NUMBER2, NUMBER3)

    print(presentation(RESULT), end='\n')
