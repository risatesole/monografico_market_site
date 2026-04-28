from ....product.usecases.get_all_products import get_all_products
from ....product import get_product_price


def customers_list():
    customers = [
        {
            "id": 1,
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "age": 28,
            "country": "USA"
        },
        {
            "id": 2,
            "name": "Carlos Méndez",
            "email": "carlos.mendez@example.com",
            "age": 35,
            "country": "Mexico"
        },
        {
            "id": 3,
            "name": "Sofia Rossi",
            "email": "sofia.rossi@example.com",
            "age": 22,
            "country": "Italy"
        },
        {
            "id": 4,
            "name": "Liam O'Connor",
            "email": "liam.oconnor@example.com",
            "age": 41,
            "country": "Ireland"
        },
        {
            "id": 5,
            "name": "Amina Hassan",
            "email": "amina.hassan@example.com",
            "age": 30,
            "country": "Egypt"
        }
    ]
    return customers

def backoffice_view_context_handler():
    """LOAD DATA"""
    products = get_all_products()
    for product in products:
        # inject price to product data
        product.current_price = get_product_price(product) # type: ignore

    context = {
        "products": products,
        "customers": customers_list()
    }
    return context
