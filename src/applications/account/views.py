from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from ...utils.env import environment
from .models import User

context = {
    "name": environment["name"],
}

def security(request): return HttpResponse("We take security very seriously")
def signIn(request): return render(request, "pages/account/signin.html", context)

def signUp(request): 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect("home")

    return render(request, "pages/account/signup.html")

def signOut(request):
    logout(request)
    return redirect("home")

# Out of project scope:
def validateAccount(request): return HttpResponse("validate account view")
def restorePassword(request): return HttpResponse("restore password view")
def changeEmail(request): return HttpResponse("change email view")
