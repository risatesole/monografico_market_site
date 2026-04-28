from .contexts.backoffice_context_handler import backoffice_view_context_handler
from django.shortcuts import render

from django.shortcuts import render, redirect
from ...product.models.model_product import Product
from ...product.models.price_model import Price

def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    return render(request, "backoffice/page.html", backoffice_view_context_handler())

def backoffice_create_product_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        price_value = request.POST.get("price")

        product = Product.objects.create(
            name=name,
            description=description,
            category=category,
            image=image,
            status="ACTIVE"
        )

        # 2. crear precio relacionado
        if price_value:
            Price.objects.create(
                product=product,
                value=price_value
            )

        return redirect("backoffice")

    return render(request, "backoffice/create/createproduct.html")



def backoffice_customer_edit_view(request): # handle the customer id fix add customer id to the request and handle it
    return render(request, "backoffice/edit/customer_edit.html")