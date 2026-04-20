from django.shortcuts import redirect
from django.contrib.auth import logout

def signoutInterface(request):
    logout(request)
    return redirect("home")
