from behave import given
import json

@given('the following products')
def load_products(context):
    for row in context.table:
        product = {
            "name": row['name'],
            "category": row['category'],
            "price": float(row['price']),
            "available": row['available'] == 'True'
        }
        # Save product logic here
