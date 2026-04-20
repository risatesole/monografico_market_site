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

        return render(request, "pages/auth/signin.html", {
            "error": "Invalid credentials"
        })

    return render(request, "pages/auth/signin.html")


# ----------------------
# SIGN OUT
# ----------------------
def signout_view(request):
    logout(request)
    return redirect("home")





#########################################################################################

from django.contrib.auth.decorators import login_required
from .models import ProviderApplicationToBeProvider


# ----------------------
# SETTINGS PAGE
# ----------------------
@login_required
def settings_view(request):
    # check if user already has an application
    application = ProviderApplicationToBeProvider.objects.filter(user=request.user).first()
    
    role = request.user.role  
    
    return render(request, "pages/auth/settings.html", {
        "application": application,
        "role": role,
    })


# ----------------------
# REQUEST PROVIDER
# ----------------------
@login_required
def request_provider_view(request):
    if request.method == "POST":
        # prevent duplicate requests
        exists = ProviderApplicationToBeProvider.objects.filter(user=request.user).exists()

        if not exists:
            ProviderApplicationToBeProvider.objects.create(
                user=request.user,
                status="pending",
                external_id="",   # you can fill later
                notes=""
            )

    return redirect("settings")

############################################################################################