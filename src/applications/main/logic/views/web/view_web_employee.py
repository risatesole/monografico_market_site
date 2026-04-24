from django.shortcuts import render
from ...usecases import setOfferStatus
from ...usecases import get_all_product_sale_requests
from ...usecases import get_all_products
from ...usecases import delete_product
from ...usecases import add_product

def employee_view(request):

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # -------------------------
        # OFFER ACTION (accept/decline)
        # -------------------------
        if form_type == "offer_action":
            offer_id = request.POST.get("offer_id")
            action = request.POST.get("action")

            if offer_id and action:
                setOfferStatus(offer_id, action)

        # -------------------------
        # DELETE PRODUCT
        # -------------------------
        elif form_type == "delete_product":
            product_id = request.POST.get("product_id")

            if product_id:
                delete_product(product_id)

        # -------------------------
        # ADD PRODUCT (WITH IMAGE)
        # -------------------------
        elif form_type == "add_product":
            name = request.POST.get("name")
            description = request.POST.get("description")
            category = request.POST.get("category")
            image = request.FILES.get("image")  # 👈 important

            if name and category:
                add_product(name, description, category, image)

    # -------------------------
    # LOAD DATA
    # -------------------------
    offers = get_all_product_sale_requests()
    products = get_all_products()

    context = {
        "providers_offers": offers,
        "products": products
    }

    return render(request, "pages/employee/page.html", context)