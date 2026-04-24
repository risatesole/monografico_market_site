from django.shortcuts import render
from .logic.usecases import setOfferStatus
from .logic.usecases import get_all_product_sale_requests
from .logic.services.product import ProductService
from .logic.usecases import get_all_products

def duck_view(request):
    if request.method == "POST":
        offer_id = request.POST.get("offer_id")
        action = request.POST.get("action")

        if action == "ACCEPTED":
            setOfferStatus(offer_id, "ACCEPTED")
        elif action == "DECLINED":
            setOfferStatus(offer_id, "DECLINED")

    offers = get_all_product_sale_requests()
    products = get_all_products()

    context = {
        'providers_offers': offers,
        'products': products
    }

    return render(request, "duck.html", context)
