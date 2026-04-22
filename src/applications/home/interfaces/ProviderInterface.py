from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import supplier_request 

def provider_request_interface(request):
    user = request.user

    application = supplier_request.objects.filter(
        user=user
    ).first()

    if request.method == "POST":
        if not application:
            supplier_request.objects.create(
                user=user,
                status="pending",
                external_id=f"REQ-{user.id}",
                notes=request.POST.get("notes", "")
            )

        return redirect("provider_request")

    return render(request, "pages/provider/request.html", {
        "application": application
    })

def provider_landing(request):
    return render(request,"pages/provider/distribuitor_landing.html")


def providerInterface(request):
    if not request.user.is_authenticated:
        return provider_landing(request)

    if request.user.role == "provider":
        return HttpResponse("Welcome provider")

    return provider_landing(request)
