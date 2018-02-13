from behave import given, when, then
from uri1007 import presentation

@given('a {number:d}')
def enter_number(context, number):
    context.number = number


@when('I present')
def I_present(context):
    context.presentation = presentation

    context.result = context.presentation(context.number)


@then('the result should be {result}')
def test_result(context, result):
    assert context.result == result
