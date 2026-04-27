# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from .modules.views.web.view_web_provider import provider_view
from .modules.backoffice.views.backoffice_view import backoffice_view
from .modules.account.user.views import signin_view, signout_view, signup_view

def home_view(request):
    return render(request, "pages/home/index.html")

urlpatterns = [
    path("", home_view, name="home"),
    path("backoffice/",backoffice_view, name="backoffice"),
    path("signin/",signin_view,name="signin"),
    path("signup/", signup_view, name="signup"),
    path("signout/", signout_view, name="signout"),
    path("provider/", provider_view, name="provider"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add this to the end of ] so it saves to the storage
