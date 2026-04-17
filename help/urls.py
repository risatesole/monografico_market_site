from django.urls import path
from .views import help

urlpatterns = [
    path("help/", help)
]
