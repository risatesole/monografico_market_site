from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.http import HttpResponse
from django.conf import settings
from django.urls import path

from .logic.views.web.view_web_provider import provider_view
from .logic.views.web.view_web_employee import employee_view
from .models import Product

def home_view(request):
    return HttpResponse("Welcome home - Django is running")

from .duck import duck
urlpatterns = [
    path("", home_view, name="home"),
    path("employee/",employee_view, name="employee"),
    path("signup/", duck, name="signup"),
    path("provider/", provider_view, name="provider"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add this to the end of ] so it saves to the storage
