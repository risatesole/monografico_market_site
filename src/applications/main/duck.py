from django.shortcuts import render, redirect

# This array lives in the server's memory, not the browser.
# It is shared by everyone and resets when the server restarts.
DUCK_STORAGE = []

def debug(request):
    print("=================================================")
    print(f"Product: {request.POST.get('product')}")
    print(f"Price: {request.POST.get('price')}")
    print("=================================================")

def duck_view(request):
    available_products = ["Rubber Duck", "Iron Duck", "Golden Duck", "something else"]

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
        'products': available_products, # Sent to the template
        'items': DUCK_STORAGE           # Your "array" of results
    }
    return render(request, "duck.html", context)


























###########################################
def duck_employee_view(request):
    context = {
        'items': DUCK_STORAGE
    }
    return render(request, "employee.html", context)
