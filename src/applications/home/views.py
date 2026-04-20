from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User



context = {
    "name": "supermercado",
}

def home(request): return render(request, "pages/home/index.html", context)
def dashboard(request): return render(request, "pages/home/dashboard.html", context)
def provider(request): return render(request, "pages/home/provider.html", context)

# ----------------------
# SIGN UP
# ----------------------
def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # prevent duplicate emails
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "error": "Email already exists"
            })

        user = User.objects.create_user(
            email=email,
            password=password,
            role="customer",
            status="active"
        )

        login(request, user)
        return redirect("home")

    return render(request, "pages/auth/signup.html")


# ----------------------
# SIGN IN
# ----------------------
def signin_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, "signin.html", {
            "error": "Invalid credentials"
        })

    return render(request, "pages/auth/signin.html")


# ----------------------
# SIGN OUT
# ----------------------
def signout_view(request):
    logout(request)
    return redirect("home")
