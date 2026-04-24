from ...models import Product
from django.core.exceptions import ValidationError

def add_product(name, description, category):
    """
    Creates a new product record. 
    Returns the Product instance if successful, or None if it fails.
    """
    try:
        # Create and save the new product instance
        new_product = Product.objects.create(
            name=name,
            description=description,
            category=category
        )
        return new_product
    except Exception as e:
        # Log the error here if needed (e.g., integrity errors or validation issues)
        print(f"Error creating product: {e}")
        return None
