from django.urls import path
from .views import security, signIn, signUp, signOut

urlpatterns = [
    path("security/", security),
    path("signin/",signIn),
    path("signout/",signOut),
    path("signup/",signUp),
]
