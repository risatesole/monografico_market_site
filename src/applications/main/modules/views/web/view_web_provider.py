from ...services.product import ProductService
from django.shortcuts import render

def find_product_by_id(product_id, available_products):
    """Find product by id or None"""
    return next(
        (p for p in available_products if str(p["id"]) == str(product_id)),
        None
    )

def provider_view(request):
    service_instance = ProductService()
    available_products = service_instance.getProducts()

    if request.method == "POST":
        product = request.POST.get("product")
        provider = request.user
        priceperbatch = request.POST.get("priceperbatch")
        batchquantity = request.POST.get("batchquantity")
        unitperbatch = request.POST.get("unitperbatch")


    context = {
        'products': available_products,
    }

    return render(request, "pages/provider/provider.html", context)

