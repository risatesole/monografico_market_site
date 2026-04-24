from ...models import Product

def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return True
    except Product.DoesNotExist:
        return False