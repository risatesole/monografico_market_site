from django.http import HttpResponse
from django.shortcuts import render
from ...utils.env import environment

context = {
    "name": environment["name"],
}

def security(request): return HttpResponse("We take security very seriously")
def signIn(request): return render(request, "pages/account/signin.html", context)
def signUp(request): return render(request, "pages/account/signup.html", context)
def signOut(request): return render(request, "pages/account/signout.html", context)

# Out of project scope:
def validateAccount(request): return HttpResponse("validate account view")
def restorePassword(request): return HttpResponse("restore password view")
def changeEmail(request): return HttpResponse("change email view")
