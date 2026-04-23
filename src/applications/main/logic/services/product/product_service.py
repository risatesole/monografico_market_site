from ....models import Product

class ProductService:

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

