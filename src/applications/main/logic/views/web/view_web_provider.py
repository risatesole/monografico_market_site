from ...usecases import get_product_sale_requests
from ...usecases import submit_product_sale_request
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
        providerid = 1 # todo: set provider
        priceperbatch = request.POST.get("priceperbatch")
        batchquantity = request.POST.get("batchquantity")
        unitperbatch = request.POST.get("unitperbatch")


        submitted_chosen_product = find_product_by_id(product, available_products)

        if submitted_chosen_product:
            submit_product_sale_request(product, providerid, priceperbatch, batchquantity,unitperbatch)

    offers = get_product_sale_requests(1)

    context = {
        'products': available_products,
        'items': offers
    }

    return render(request, "pages/provider/provider.html", context)