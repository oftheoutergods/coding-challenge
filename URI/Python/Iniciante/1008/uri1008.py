'''
uri 1008
'''


def number_presents(number):
    return "NUMBER = %i" % number


def salary_presents(salary):
    return "SALARY = U$ %.2f" % salary


def calc_salary(hours, perhour):
    return hours * perhour


if __name__ == '__main__':
    NUMBER = int(input())
    HOURS = int(input())
    PERHOUR = float(input())
    SALARY = calc_salary(HOURS, PERHOUR)

    print(number_presents(NUMBER))
    print(salary_presents(SALARY), end='\n')
