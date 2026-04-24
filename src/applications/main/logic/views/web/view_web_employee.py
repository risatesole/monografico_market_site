from django.shortcuts import render
from ...usecases import (
    setOfferStatus,
    get_all_product_sale_requests,
    get_all_products,
    delete_product,
    add_product
)

def form_action_set_offer_status(request, form_type):
    """PROVIDER OFFER ACTION (accept/decline)"""
    if form_type == "offer_action":
        offer_id = request.POST.get("offer_id")
        action = request.POST.get("action")

        if offer_id and action:
            setOfferStatus(offer_id, action)


def form_action_delete_product(request, form_type):
    """DELETE PRODUCT"""
    if form_type == "delete_product":
        product_id = request.POST.get("product_id")

        if product_id:
            delete_product(product_id)


def form_action_add_product(request, form_type):
    """ADD PRODUCT WITH IMAGE"""
    if form_type == "add_product":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        image = request.FILES.get("image")

        if name and category:
            add_product(name, description, category, image)


def employee_view(request):
    """HANDLE POST ACTIONS"""
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type:
            form_action_set_offer_status(request, form_type)
            form_action_delete_product(request, form_type)
            form_action_add_product(request, form_type)

    """LOAD DATA"""
    offers = get_all_product_sale_requests()
    products = get_all_products()

    context = {
        "providers_offers": offers,
        "products": products
    }

    return render(request, "pages/employee/page.html", context)