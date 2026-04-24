from django.shortcuts import render
from .logic.usecases import setOfferStatus
from .logic.usecases import get_all_product_sale_requests
from .logic.services.product import ProductService
from .logic.usecases import get_all_products, delete_product

def duck_view(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # Handle offer actions
        if form_type == "offer_action":
            offer_id = request.POST.get("offer_id")
            action = request.POST.get("action")

            if offer_id and action:
                if action == "ACCEPTED":
                    setOfferStatus(offer_id, "ACCEPTED")
                elif action == "DECLINED":
                    setOfferStatus(offer_id, "DECLINED")

        # Handle product deletion
        elif form_type == "delete_product":
            product_id = request.POST.get("product_id")

            if product_id:
                delete_product(product_id)

    offers = get_all_product_sale_requests()
    products = get_all_products()

    context = {
        "providers_offers": offers,
        "products": products
    }

    return render(request, "duck.html", context)