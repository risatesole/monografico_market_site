from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User , ProviderApplicationToBeProvider
from .interfaces.signupInterface import signup_interface
from .interfaces.signinInterface import signinInterface
from .interfaces.signoutInterface import signoutInterface
from .interfaces.ProviderInterface import providerInterface

context = {
    "name": "supermercado",
}

def home(request): return render(request, "pages/home/index.html", context)
def dashboard(request): return render(request, "pages/home/dashboard.html", context)
def provider(request): return render(request, "pages/home/provider.html", context)
def signup_view(request): return signup_interface(request)
def signin_view(request): return signinInterface(request)
def signout_view(request): return signoutInterface(request)

def apply_to_be_provider_view(request):
    return apply_to_be_provider(request)

def settings_view(request):
    if not request.user.is_authenticated:
        return redirect("home")

    return HttpResponse("this is settings page")


from .interfaces.ProviderInterface import provider_request_interface

def provider_view(request):
    return providerInterface(request)

def provider_request_view(request):
    return provider_request_interface(request)
