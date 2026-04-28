from .contexts.backoffice_context_handler import backoffice_view_context_handler
from django.shortcuts import render

def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    return render(request, "backoffice/page.html", backoffice_view_context_handler())




from django.shortcuts import render, redirect
from ...product.models.model_product import Product

def backoffice_create_product_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        image = request.FILES.get("image")

        Product.objects.create(
            name=name,
            description=description,
            category=category,
            image=image
        )

        return redirect("backoffice")  # cambia esto por tu ruta real

    return render(request, "backoffice/create/createproduct.html")