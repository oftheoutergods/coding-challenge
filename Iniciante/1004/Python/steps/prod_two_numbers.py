from behave import given, when, then
from uri1004 import prod_two_numbers


@given('I have entered {number1:d}')
def enter_number1(context, number1):
    context.number1 = number1


@given('I have also entered {number2:d}')
def enter_number2(context, number2):
    context.number2 = number2


@when('I prod')
def call_prod(context):

    context.prod_two_numbers = prod_two_numbers

    context.result = context.prod_two_numbers(context.number1, context.number2)


@then('the prod should be {result:d}')
def check_result(context, result):
    assert context.result == result
