from ....product import set_product_price
from ....usecases import get_all_products

def employee_action_set_product_price(request,form_type):
    if form_type == "set_price":
        product_id = request.POST.get("product_id")
        value = request.POST.get("price")

        product = get_all_products().get(id=product_id)
        set_product_price(product, value)
