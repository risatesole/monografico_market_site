# from .....services.price.service_price import PriceService
from ....services.price.service_price import PriceService 
from ....usecases import get_all_products

def employee_action_set_product_price(request,form_type):
    priceservice = PriceService()

    if form_type == "set_price":
        product_id = request.POST.get("product_id")
        value = request.POST.get("price")

        product = get_all_products().get(id=product_id)
        priceservice.set_product_price(product, value)
