from django.shortcuts import render

def employee_action_delete_product(request, form_type):
    pass # todo: problems with delete product circular dependency
    """DELETE PRODUCT"""
    # if form_type == "delete_product":
    #     product_id = request.POST.get("product_id")
    #     if product_id:
    #         delete_product(product_id)
