from django.shortcuts import render
from .logic.services.provider import ProviderService
from .models import Product

# Fake database:
ITEMS = []

def debug(request):
    print("=================================================")
    print(f"items: {ITEMS}")
    print(f"Product: {request.POST.get('product')}")
    print(f"Price: {request.POST.get('price')}")
    print(f"Quantity: {request.POST.get('quantity')}")
    print("=================================================")




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




def submit_product_sale_request(providerid,productid,quantity,price):
    """Submit a provider's request to sell a product for later approval or rejection."""
    provider_service = ProviderService()
    provider_service.setRequestSellProduct(providerid,productid,quantity,price)



# simple in-memory storage (for testing only)


def duck_view(request):
    service_instance = ProductService()
    provider_service = ProviderService()
    available_products = service_instance.getProducts()

    if request.method == "POST":
        product_id = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        # find product by id
        submitted_chosen_product = next(
            (p for p in available_products if str(p["id"]) == product_id),
            None
        )

        if submitted_chosen_product:
            submit_product_sale_request(1,product_id,quantity,price)


    context = {
        'products': available_products
        # 'items': ITEMS
    }

    return render(request, "duck.html", context)





























###########################################
def duck_employee_view(request):
    context = {
        'items': ITEMS
    }
    return render(request, "employee.html", context)
