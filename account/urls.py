from django.urls import path
from .views import security

urlpatterns = [
    path("security/", security),
]
