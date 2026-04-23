from django.shortcuts import render
from .logic.handler import get_all_product_sale_requests, setOfferStatus
from .logic.services.product import ProductService

def duck_view(request):
    if request.method == "POST":
        offer_id = request.POST.get("offer_id")
        action = request.POST.get("action")

        if action == "ACCEPTED":
            setOfferStatus(offer_id, "ACCEPTED")
        elif action == "DECLINED":
            setOfferStatus(offer_id, "DECLINED")

    offers = get_all_product_sale_requests()
    context = {'providers_offers': offers}

    return render(request, "duck.html", context)







###########################################
def duck_employee_view(request):
    context = {
        'items': ITEMS
    }
    return render(request, "employee.html", context)
