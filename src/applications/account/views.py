from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import logout
from ...utils.env import environment
from .handler.SignupHandler import signUpHandler

context = {
    "name": environment["name"],
}

def security(request): return HttpResponse("We take security very seriously")
def signIn(request): return render(request, "pages/account/signin.html", context)

def signUp(request): 
    return signUpHandler(request)

def signOut(request):
    logout(request)
    return redirect("home")

# Out of project scope:
def validateAccount(request): return HttpResponse("validate account view")
def restorePassword(request): return HttpResponse("restore password view")
def changeEmail(request): return HttpResponse("change email view")
