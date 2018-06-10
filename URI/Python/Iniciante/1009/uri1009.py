"""
uri 1009

Name is a string
repr. the seller's name

FixedSalary is a float
repr. the fixed salary of a seller

SalesInMonth is a float
repr. how many the seller made in a month

Bonus is a float
repr. the bonus over the SalesInMonth

SalaryTotal
repr. the fixed salary with bonus

Message is a string
repr. the output
"""


BONUS_RATE = 0.15

def output(total):
    """
    SalaryTotal -> Message
    """
    return "TOTAL = R$ %.2f" % total


def bonus(sales_month):
    """
    SalesInMonth -> Bonus
    """
    return sales_month * BONUS_RATE


def total_salary(fixed, sales_month):
    """
    FixedSalary, SalesInMonth -> SalaryTotal
    """
    return fixed + bonus(sales_month)


if __name__ == "__main__":
    NAME = input()
    SALARY = float(input())
    SALES = float(input())

    TOTAL = total_salary(SALARY, SALES)
    print(output(TOTAL))
