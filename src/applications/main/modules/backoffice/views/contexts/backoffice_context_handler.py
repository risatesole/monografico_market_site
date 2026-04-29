from ....account.user.models.customer_profile import Customer as Customer
from ....account.user.models.employee_profile import Employee
from ....product.models.model_product import Product
from ....product.models.price_model import Price

def inventory_stock(products):
    inventory = []

    for product in products:
        inventory.append({
            "id": product.id,
            "name": product.name,
            "stock": getattr(product, "stock", 0),
            "unit": "kg",
            "status": "Low" if getattr(product, "stock", 0) < 20 else "Normal",
        })

    return inventory

def backoffice_view_context_handler():
    customers = Customer.objects.select_related("user").all()
    employees = Employee.objects.select_related("user").all()

    products = Product.objects.prefetch_related("prices").all()

    for product in products:
        latest_price = product.prices.first() # type: ignore
        product.current_price = latest_price.value if latest_price else 0 # type: ignore


    mock_provider_data = [{     
        "name": "proveedor1",
        "phone_number": "1 (829)-123-4567",
        "address": "Avenida casa viva",
        "email": "provider1@provider.com",
        "description": "vende flores"
    }]

    context = {
        "customers": customers,
        "employees": employees,
        "providers": mock_provider_data,
        "products": products,
        "inventory": inventory_stock(products),
        "project":{
            "name": "Duck"
        }
    }

    return context
