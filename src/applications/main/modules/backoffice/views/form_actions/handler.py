from .set_offer_status import employee_action_set_offer_status
from .delete_product import employee_action_delete_product
from .set_product_price import employee_action_set_product_price
from .add_product import employee_action_add_product

def form_actions_handler(request, form_type):
    employee_action_set_offer_status(request, form_type)
    employee_action_delete_product(request, form_type)
    employee_action_add_product(request, form_type)
    employee_action_set_product_price(request,form_type)

