from behave import given, when, then
from uri1002 import presentation


@given('a {number:f}')
def enter_number(context, number):
    context.number = number


@when('I present')
def i_present(context):
    context.presentation = presentation

    context.result = context.presentation(context.number)


@then('the presentation should be {result}')
def check_result(context, result):
    assert context.result == result
