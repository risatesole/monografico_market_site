from django.http import HttpResponse
from django.shortcuts import render, redirect
from .interfaces.signinInterface import signinInterface
from .interfaces.signupInterface import signup_interface
from .interfaces.signoutInterface import signoutInterface
from .interfaces.ProviderInterface import providerInterface
from .interfaces.ProviderInterface import provider_request_interface
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from .models import ProviderApplicationToBeProvider

context = {
    "name": "Supermercado Blanco",
}

def home(request): return render(request, "pages/home/index.html", context)
# def dashboard(request): return render(request, "pages/home/dashboard.html", context)
def provider(request): return render(request, "pages/home/provider.html", context)
def signin_view(request): return signinInterface(request)

def signout_view(request): return signoutInterface(request)

def settings_view(request):
    if not request.user.is_authenticated:
        return redirect("home")

    return HttpResponse("this is settings page")

def provider_view(request):
    return providerInterface(request)

@login_required
def provider_request_view(request):
    """
    todo when the user loads this request page if the user is not logged in 
    it should redirect to log in, once the user hits signin, it should return to the /provider/request,
    actualmente no lo hace, se lo dejo al yo de el futuro para que lo arregle cuando este haciendo final 
    touches
    """
    if not request.user.is_authenticated:
        return redirect(f"/signin?next=/provider/request/")

    return provider_request_interface(request)

