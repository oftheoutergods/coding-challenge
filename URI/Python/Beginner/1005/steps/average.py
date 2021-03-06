from behave import given, when, then
from uri1005 import average


@given('a {number1:f}')
def enter_number1(context, number1):
    context.number1 = number1


@given('a another {number2:f}')
def enter_number2(context, number2):
    context.number2 = number2


@when('I calculate')
def calculate(context):
    context.average = average

    context.result = context.average(context.number1, context.number2)


@then('the average should be {result:f}')
def check_result(context, result):
    assert context.result == result
