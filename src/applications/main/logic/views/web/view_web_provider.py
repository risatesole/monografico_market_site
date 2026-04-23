from ...handler import get_product_sale_requests
from ...usecases import submit_product_sale_request
from ...services.product import ProductService
from django.shortcuts import render

def provider_view(request):
    service_instance = ProductService()
    available_products = service_instance.getProducts()
    # available_products = service_instance.getProducts()

    if request.method == "POST":
        product_id = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        # find product by id
        submitted_chosen_product = next(
            (p for p in available_products if str(p["id"]) == product_id),
            None
        )

        if submitted_chosen_product:
            submit_product_sale_request(1,product_id,quantity,price)

    offers = get_product_sale_requests(1)
    context = {'products': available_products,'items': offers }
    return render(request, "pages/provider/provider.html", context)

