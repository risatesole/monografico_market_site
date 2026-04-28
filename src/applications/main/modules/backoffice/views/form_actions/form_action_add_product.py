from django.shortcuts import render
from ....product import add_product

def employee_action_add_product(request, form_type):
    """ADD PRODUCT WITH IMAGE"""
    if form_type == "add_product":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        image = request.FILES.get("image")

        if name and category:
            add_product(name, description, category, image)
