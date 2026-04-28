from .contexts.backoffice_context_handler import backoffice_view_context_handler
from django.shortcuts import render,redirect, get_object_or_404 
from ...product.models.model_product import Product
from ...product.models.price_model import Price
from ...account.user.models.customer_profile import Customer


def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    return render(request, "backoffice/page.html", backoffice_view_context_handler())

def backoffice_create_product_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        price_value = request.POST.get("price")

        product = Product.objects.create(
            name=name,
            description=description,
            category=category,
            image=image,
            status="ACTIVE"
        )

        # 2. crear precio relacionado
        if price_value:
            Price.objects.create(
                product=product,
                value=price_value
            )

        return redirect("backoffice")

    return render(request, "backoffice/create/createproduct.html")


def backoffice_customer_edit_view(request, customer_id):
    customer = Customer.objects.select_related("user").filter(id=customer_id).first()

    if not customer or customer.user.role != "customer":
        return redirect("backoffice")

    if request.method == "POST":
        user = customer.user
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.role = request.POST.get("role")
        user.save()

        customer.phone = request.POST.get("phone")
        customer.address = request.POST.get("address")
        customer.save()

        return redirect("customer_edit", customer_id=customer.id) # type: ignore

    return render(request, "backoffice/edit/customer_edit.html", {
        "customer": customer
    })
