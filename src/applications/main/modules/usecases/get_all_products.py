# todo: relocate this method to product module
from ...models import Product

def get_all_products():
    return Product.objects.all()
