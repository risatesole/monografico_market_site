from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import ProviderApplicationToBeProvider

@login_required
def apply_to_be_provider(request):
    if request.method == "POST":
        # Check if an application already exists to avoid duplicates
        exists = ProviderApplicationToBeProvider.objects.filter(user=request.user).exists()
        
        if not exists:
            ProviderApplicationToBeProvider.objects.create(
                user=request.user,
                status="pending",
                external_id=f"REQ-{request.user.id}", # Placeholder ID
                notes=request.POST.get("notes", "")
            )
            
    return redirect('settings_page') # Redirect back to the settings interface

@login_required
def settingsPageInterface(request):
    application = ProviderApplicationToBeProvider.objects.filter(user=request.user).first()
    role = request.user.role  
    
    return render(request, "pages/auth/settings.html", {
        "application": application,
        "role": role,
    })
