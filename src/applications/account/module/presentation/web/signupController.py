from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from ....module.application.signup_Service import SignupService
from ....module.domain.entities.user.UserEntity import UserEntity

from datetime import date

class SignupController:
    def __init__(self) -> None:
        pass
    
    def render(self,request:HttpRequest):
        if request.method == "POST":
            """
            # todo: 
            user:UserEntity = UserEntity(
                0,
                request.POST["email"],
                request.POST["password"],
                request.POST["first_name"],
                request.POST["last_name"],
                date.today(),
                date.today(),
                True,
                False
                )
            pass
            signup = SignupService()
            signup.execute(user:UserEntity)
            """
        return render(request, "pages/account/signup.html")
