from django.urls import path
from .views import home , dashboard, provider

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("provider/", provider, name="provider"), 
]