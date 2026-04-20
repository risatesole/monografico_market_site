from django.shortcuts import render, redirect

def provider_landing(request):
    return render(request,"pages/provider/distribuitor_landing.html")










# export functions

from ..models import ProviderApplicationToBeProvider

def provider_request_interface(request):
    context = {
        
    }
    return render(request, "pages/provider/request.html", {})



def providerInterface(request):
    return provider_landing(request)
