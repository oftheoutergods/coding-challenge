#import sys
#sys.path.append('..')

from behave import given, when, then
from uri1001 import sum_two_numbers


@given('I have entered {number1:d}')
def enter_number1(context, number1):
    context.number1 = number1


@given('I have also entered {number2:d}')
def enter_number2(context, number2):
    context.number2 = number2


@when('I sum')
def call_sum(context):

    context.sum_two_numbers = sum_two_numbers

    context.result = context.sum_two_numbers(context.number1, context.number2)


@then('the sum should be {result:d}')
def check_result(context, result):
    assert context.result == result
