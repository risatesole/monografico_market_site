from ....usecases import get_all_products
from ....product import get_product_price

def backoffice_view_context_handler():
    """LOAD DATA"""
    products = get_all_products()
    for product in products:
        # inject price to product data
        product.current_price = get_product_price(product) # type: ignore

    context = {
        "products": products
    }
    return context
