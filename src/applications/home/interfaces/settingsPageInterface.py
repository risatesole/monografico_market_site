from django.shortcuts import render, redirect
from ..models import ProviderApplicationToBeProvider

def settingsPageInterface(request):
        # check if user already has an application
    application = ProviderApplicationToBeProvider.objects.filter(user=request.user).first()
    
    role = request.user.role  
    
    return render(request, "pages/auth/settings.html", {
        "application": application,
        "role": role,
    })

