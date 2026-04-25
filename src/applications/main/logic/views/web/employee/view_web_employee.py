from .form_actions import (
    employee_action_delete_product,
    employee_action_set_offer_status,
    employee_action_add_product
)

from ....usecases import get_all_product_sale_requests, get_all_products
from django.shortcuts import render
from .....models import Price


def get_product_price(product):
    last_price = product.prices.first()
    return last_price.value if last_price else None


def set_product_price(product, value):
    return Price.objects.create(
        product=product,
        value=value
    )


def employee_view(request):
    """HANDLE POST ACTIONS"""
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type:
            employee_action_set_offer_status(request, form_type)
            employee_action_delete_product(request, form_type)
            employee_action_add_product(request, form_type)

            # 👇 ADD PRICE ACTION HERE (optional future hook)
            if form_type == "set_price":
                product_id = request.POST.get("product_id")
                value = request.POST.get("price")

                product = get_all_products().get(id=product_id)
                set_product_price(product, value)

    """LOAD DATA"""
    offers = get_all_product_sale_requests()
    products = get_all_products()

    for product in products:
        product.current_price = get_product_price(product)

    context = {
        "providers_offers": offers,
        "products": products
    }

    return render(request, "pages/employee/page.html", context)