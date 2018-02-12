from behave import given, when, then
from uri1002 import circle_area


@given('a {number:f}')
def enter_number(context, number):
    context.number = number


@when('I computes the area')
def calculate_area(context):
    context.circle_area = circle_area

    context.result = context.circle_area(context.number)


@then('the area should be {result:f}')
def check_result(context, result):
    assert context.result == result
