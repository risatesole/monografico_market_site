from django.shortcuts import render
from .logic.services.provider import ProviderService
from .models import Product
from .logic.handler import submit_product_sale_request
from .logic.services.product import ProductService

# Fake database:
ITEMS = []

def debug(request):
    print("=================================================")
    print(f"items: {ITEMS}")
    print(f"Product: {request.POST.get('product')}")
    print(f"Price: {request.POST.get('price')}")
    print(f"Quantity: {request.POST.get('quantity')}")
    print("=================================================")




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
