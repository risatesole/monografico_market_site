from django.urls import path
# from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Product

from django.conf import settings
from django.conf.urls.static import static

def example_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("image")

        if name and image:
            Product.objects.create(name=name, image=image)
            return redirect("/")

    products = Product.objects.all()

    return render(request, "duck/page.html", {
        "products": products
    })

urlpatterns = [
    path("", example_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add this to the end of ] so it saves to the storage

