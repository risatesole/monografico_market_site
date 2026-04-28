# todo: relocate this method to product module
from ...models import Product

def add_product(name, description, category, image=None):
    """
    Creates a new product with optional image.
    Returns Product or None.
    """
    try:
        product = Product.objects.create(
            name=name,
            description=description,
            category=category,
            image=image
        )
        return product

    except Exception as e:
        print(f"[ERROR] creating product: {e}")
        return None