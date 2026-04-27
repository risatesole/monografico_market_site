from ...usecases import get_all_product_sale_requests, get_all_products
from django.shortcuts import render
from ...services.price.service_price import PriceService
from .form_actions.handler import form_actions_handler

def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type:
            """FORM ACTIONS/HANDLERS"""
            form_actions_handler(request, form_type)

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
