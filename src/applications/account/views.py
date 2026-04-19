from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from ...utils import environment
from .module.presentation.web.signupController import SignupController

context: dict[str, str] = {
    "name": environment["name"],
}

def security(request: HttpRequest) -> HttpResponse:
    return HttpResponse("We take security very seriously")

def signIn(request: HttpRequest) -> HttpResponse: 
    response: HttpResponse = render(request, "pages/account/signin.html", context)
    return response

def signUp(request: HttpRequest) -> HttpResponse: 
    controller = SignupController()
    return controller.render(request)

def signOut(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("home")

def validateAccount(request: HttpRequest) -> HttpResponse: 
    return HttpResponse("validate account view")

def restorePassword(request: HttpRequest) -> HttpResponse: 
    return HttpResponse("restore password view")

def changeEmail(request: HttpRequest) -> HttpResponse: 
    return HttpResponse("change email view")