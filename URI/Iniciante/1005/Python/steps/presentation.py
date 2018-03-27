from behave import given, when, then
from uri1005 import presentation

@given('a {number:f}')
def enter_number(context, number1):
    context.number = number1
    print(context.number1)


@when('I present')
def present(context):
    context.presentation = presentation
    context.result = context.presentation(context.number1)


@then('the result should be {result}')
def check_result(context, result):
    assert context.result == result
