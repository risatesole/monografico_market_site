from django.shortcuts import render, redirect
from django.contrib.auth import login
from .logic.services.user.user_service import UserService, emailExistsError

# todo: fix error of when user signsup with used email it throws in strange ways
def duck(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        service = UserService()

        try:
            user = service.createCustomer(first_name, last_name, email, password)
            login(request, user)
            return redirect("home")

        except emailExistsError:
            print("Email already exists")
            return render(request, "pages/auth/signup.html", {
                "error": "Email already exists"
            })

    return render(request, "pages/auth/signup.html")


