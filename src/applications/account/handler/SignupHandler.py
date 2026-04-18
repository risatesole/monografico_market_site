from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import login
from ....utils.env import environment
from ..models import User

def signUpHandler(request): 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")
    return render(request, "pages/account/signup.html")
