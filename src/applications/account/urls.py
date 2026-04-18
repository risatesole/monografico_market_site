from django.urls import path
from .views import security, signIn, signUp, signOut,restorePassword

urlpatterns = [
    path("security/", security, name="security"),
    path("signin/", signIn, name="signin"),
    path("signout/",signOut,name= "signout"),
    path("signup/", signUp, name="signup"),
    path("restorepassword", restorePassword,name="restorepassword"),
]
