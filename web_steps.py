from behave import then

@then('I should see the product "{product_name}"')
def verify_product_in_response(context, product_name):
    assert product_name in context.response.text

@then('the product price should be "{price}"')
def verify_product_price(context, price):
    assert str(price) in context.response.text
