from django.shortcuts import render
from .logic.services.provider import ProviderService
from .models import Product
from .logic.handler import submit_product_sale_request, get_product_sale_requests
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




























###########################################
def duck_employee_view(request):
    context = {
        'items': ITEMS
    }
    return render(request, "employee.html", context)
