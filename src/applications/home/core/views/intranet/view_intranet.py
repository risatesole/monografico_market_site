from django.contrib.auth.decorators import login_required
from ....models import User, ProviderApplicationToBeProvider
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def intranet_view(request):
    """
    This is the company employees facing part of the application
    if the user can see this should be in internal_user role
    if the user is a customer or a provider, it should not load, eg.
    redirect to home page
    """
    if request.user.role == 'internal_user':
        context = {}
        return render(request, "pages/intranet/page.html", context)
    return redirect('home')

def intranet_provider_applicationview(request):
    """
    This view manages the applications to be a provider sent by the users
    it should show the list of applications
    """
    if request.user.role == 'internal_user':

        list_users = User.objects.all()
        provider_applications = ProviderApplicationToBeProvider.objects.all()
        context = {
            "list_users": list_users,
            "provider_applications": provider_applications
        }
        return render(request, "pages/intranet/providerApplications/providerApplications.html", context)

def intranet_provider_applications_details_view(request,id):
    if request.user.role == 'internal_user':
        application = get_object_or_404(ProviderApplicationToBeProvider, pk=id)
        context = {
            "application": application
        }
        return render(request, "pages/intranet/providerApplications/provider_Applications_details.html", context)
    return redirect('home')
