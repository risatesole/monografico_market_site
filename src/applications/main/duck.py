from django.shortcuts import render, redirect

# This array lives in the server's memory, not the browser.
# It is shared by everyone and resets when the server restarts.
DUCK_STORAGE = []

def debug(request):
    print("=================================================")
    print(f"Product: {request.POST.get('product')}")
    print(f"Price: {request.POST.get('price')}")
    print("=================================================")


class ProductService:
    def getAvialableProducts(self) -> list[str]:
        """Returns a list of products currently in stock."""
        return ["Rubber Duck", "Iron Duck", "Golden Duck", "Something Else"]


def duck_view(request):
    service_instance = ProductService() 
    available_products = service_instance.getAvialableProducts() # type: ignore

    if request.method == "POST":
        product = request.POST.get("product")
        price = request.POST.get("price")

        if product and price:
            DUCK_STORAGE.append({
                'product': product,
                'price': price
            })
        return redirect('duck')

    context = {
        'products': available_products, 
        'items': DUCK_STORAGE           
    }
    return render(request, "duck.html", context)


























###########################################
def duck_employee_view(request):
    context = {
        'items': DUCK_STORAGE
    }
    return render(request, "employee.html", context)
