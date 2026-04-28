from .....models import Product

class ProductService:
    """
    Service layer for handling Product-related operations.

    This class provides methods to retrieve and create Products
    using the underlying Product model.
    """

    def getProducts(self) -> list[dict]:
        products = Product.objects.all()

        return [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "category": product.category
            }
            for product in products
        ]

    def setProduct(self, name, description, category):
        product = Product.objects.create(
            name=name,
            description=description,
            category=category
        )
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "category": product.category
        }

