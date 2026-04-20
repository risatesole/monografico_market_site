from django.urls import path
from .views import home , dashboard, provider, signin_view, signout_view, signup_view, settings_view, request_provider_view

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("provider/", provider, name="provider"), 


    path("signin/", signin_view, name="signin"), 
    path("signout/", signout_view, name="signout"), 
    path("signup/", signup_view, name="signup"), 

    path("settings/", settings_view, name="settings"),
    path("request-provider/", request_provider_view, name="request_provider"),
]