from django.shortcuts import render

# Fake database:
ITEMS = []

def debug(request):
    print("=================================================")
    print(f"items: {ITEMS}")
    print(f"Product: {request.POST.get('product')}")
    print(f"Price: {request.POST.get('price')}")
    print(f"Quantity: {request.POST.get('quantity')}")
    print("=================================================")



def duck_view(request):
    context={}
    return render(request,"duck.html",context)










###########################################
def duck_employee_view(request):
    context = {
        'items': ITEMS
    }
    return render(request, "employee.html", context)
