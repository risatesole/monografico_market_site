from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..models import User

def signup_interface(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "error": "Email already exists"
            })

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role="customer",
            status="active"
        )

        login(request, user)
        return redirect("home")

    return render(request, "pages/auth/signup.html")
