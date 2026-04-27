from ...views.web.employee.form_actions import (
    employee_action_set_offer_status
)
from .form_actions.delete_product import employee_action_delete_product
from .form_actions.set_product_price import employee_action_set_product_price
from .form_actions.add_product import employee_action_add_product

from ...usecases import get_all_product_sale_requests, get_all_products
from django.shortcuts import render
from ...services.price.service_price import PriceService

def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type:
            """FORM ACTIONS/HANDLERS"""
            employee_action_set_offer_status(request, form_type)
            employee_action_delete_product(request, form_type)
            employee_action_add_product(request, form_type)
            employee_action_set_product_price(request,form_type)

    """LOAD DATA"""
    price_service = PriceService()
    offers = get_all_product_sale_requests()
    products = get_all_products()
    for product in products:
        # inject price to product data
        product.current_price = price_service.get_product_price(product) # type: ignore

    context = {
        "providers_offers": offers,
        "products": products
    }

    return render(request, "pages/employee/page.html", context)