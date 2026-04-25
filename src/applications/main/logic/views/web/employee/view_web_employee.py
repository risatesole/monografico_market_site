from .form_actions import employee_action_delete_product , employee_action_set_offer_status, employee_action_add_product
from ....usecases import get_all_product_sale_requests, get_all_products
from django.shortcuts import render

def employee_view(request):
    """HANDLE POST ACTIONS"""
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type:
            employee_action_set_offer_status(request, form_type)
            employee_action_delete_product(request, form_type)
            employee_action_add_product(request, form_type)

    """LOAD DATA"""
    offers = get_all_product_sale_requests()
    products = get_all_products()

    context = {
        "providers_offers": offers,
        "products": products
    }

    return render(request, "pages/employee/page.html", context)