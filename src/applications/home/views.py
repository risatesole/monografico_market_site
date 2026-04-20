from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User , ProviderApplicationToBeProvider
from .interfaces.signupInterface import signup_interface
from .interfaces.signinInterface import signinInterface
from .interfaces.signoutInterface import signoutInterface
from .interfaces.settingsPageInterface import settingsPageInterface

context = {
    "name": "supermercado",
}

def home(request): return render(request, "pages/home/index.html", context)
def dashboard(request): return render(request, "pages/home/dashboard.html", context)
def provider(request): return render(request, "pages/home/provider.html", context)
def signup_view(request): return signup_interface(request)
def signin_view(request): return signinInterface(request)
def signout_view(request): return signoutInterface(request)
@login_required
def settings_view(request): return settingsPageInterface

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