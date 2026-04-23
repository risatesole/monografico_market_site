from django.urls import path
# from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Product

from django.conf import settings
from django.conf.urls.static import static
from .views import shared_view, provider_view

def example_view(request):
    if request.method == "POST":

        # DELETE
        if "delete_id" in request.POST:
            product = Product.objects.get(id=request.POST.get("delete_id"))
            product.delete()
            return redirect("/duck/")

        # EDIT
        if "edit_id" in request.POST:
            product = Product.objects.get(id=request.POST.get("edit_id"))
            new_name = request.POST.get("new_name")

            if new_name:
                product.name = new_name
                product.save()

            return redirect("/duck/")

        # CREATE
        name = request.POST.get("name")
        image = request.FILES.get("image")

        if name and image:
            Product.objects.create(name=name, image=image)
            return redirect("home")

    products = Product.objects.all()

    return render(request, "duck/page.html", {
        "products": products
    })

urlpatterns = [
    # path("", example_view,name="home"),
    path("", shared_view, name="shared"),
    path("provider/", provider_view, name="provider")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add this to the end of ] so it saves to the storage

