from behave import given, when, then
from uri1007 import difference

@given('a first {number1:d}')
def enter_number1(context, number1):
    context.number1 = number1


@given('a second {number2:d}')
def enter_number2(context, number2):
    context.number2 = number2
    print(number2)

@given('a third {number3:d}')
def enter_number3(context, number3):
    context.number3 = number3

@given('a fourth {number4:d}')
def enter_number4(context, number4):
    context.number4 = number4


@when('I calculate')
def calculate(context):
    context.difference = difference

    context.result = context.difference(context.number1, context.number2, context.number3, context.number4)


@then('the result should be {result:d}')
def check_result(context, result):
    assert context.result == result
