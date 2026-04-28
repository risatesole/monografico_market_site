from django.shortcuts import render
from ....usecases.delete_product import delete_product

def employee_action_delete_product(request, form_type):
    """DELETE PRODUCT"""
    if form_type == "delete_product":
        product_id = request.POST.get("product_id")
        if product_id:
            delete_product(product_id)
