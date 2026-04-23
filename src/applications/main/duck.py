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
    if request.method == "POST":
        # Run your debug print
        debug(request)

        product = request.POST.get("product")
        price = request.POST.get("price")

        # Store directly into the global list
        if product and price:
            DUCK_STORAGE.append({
                'product': product,
                'price': price
            })

        # Redirect back to the GET view
        return redirect('duck')

    # Render the current state of the global list
    context = {
        'items': DUCK_STORAGE
    }
    return render(request, "duck.html", context)



























###########################################
def duck_employee_view(request):
    context = {
        'items': DUCK_STORAGE
    }
    return render(request, "employee.html", context)
