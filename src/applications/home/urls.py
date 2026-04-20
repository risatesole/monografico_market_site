from django.urls import path
from .views import home , dashboard, provider, signin_view, signout_view, signup_view

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("provider/", provider, name="provider"), 


    path("signin/", signin_view, name="signin"), 
    path("signout/", signout_view, name="signout"), 
    path("signup/", signup_view, name="signup"), 
]