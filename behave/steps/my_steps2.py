from behave import given, when, then

@given('I have entered {number1:d} into the calculator and I have entered {number2:d} into the calculator')
def step_impl(context, number1, number2):
    context.number1 = number1
    context.number2 = number2

@when('I press add')
def step_impl(context):
    context.result = context.number1 + context.number2

@then('the result should be {expected_result:d} on the screen')
def step_impl(context, expected_result):
    print(context.result)
    print(expected_result)
    assert context.result == expected_result

