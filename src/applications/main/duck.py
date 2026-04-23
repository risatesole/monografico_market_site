from django.shortcuts import render

def debug(request):
    print("=================================================")
    print(f"Product: {request.POST.get('product')}")
    print(f"Price: {request.POST.get('price')}")
    print(f"Quantity: {request.POST.get('quantity')}")
    print("=================================================")


class ProductService:
    def getAvailableProducts(self) -> list[dict]:
        return [
            {
                "id": 1,
                "name": "leche listamilk",
                "category": "lacteos"
            },
            {
                "id": 2,
                "name": "leche rica",
                "category": "lacteos"
            }
        ]


# simple in-memory storage (for testing only)
ITEMS = []

def duck_view(request):
    service_instance = ProductService()
    available_products = service_instance.getAvailableProducts()

    if request.method == "POST":
        product_id = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        debug(request)

        # find product by id
        selected_product = next(
            (p for p in available_products if str(p["id"]) == product_id),
            None
        )

        if selected_product:
            ITEMS.append({
                "product": selected_product["name"],
                "price": price,
                "quantity": quantity
            })

    context = {
        'products': available_products,
        'items': ITEMS
    }

    return render(request, "duck.html", context)





























###########################################
def duck_employee_view(request):
    context = {
        'items': ITEMS
    }
    return render(request, "employee.html", context)
