from ....usecases import get_all_product_sale_requests, get_all_products
from ....product import get_product_price


def backoffice_view_context_handler():
    """LOAD DATA"""
    offers = get_all_product_sale_requests()
    products = get_all_products()
    for product in products:
        # inject price to product data
        product.current_price = get_product_price(product) # type: ignore

    context = {
        "providers_offers": offers,
        "products": products
    }
    return context
