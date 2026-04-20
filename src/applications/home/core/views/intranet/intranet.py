@login_required
def intranet_view(request):
    """
    This is the company employees facing part of the application
    if the user can see this should be in internal_user role
    if the user is a customer or a provider, it should not load, eg.
    redirect to home page
    """
    if request.user.role == 'internal_user':

        list_users = User.objects.all()
        provider_applications = ProviderApplicationToBeProvider.objects.all()
        context = {
            "list_users": list_users,
            "provider_applications": provider_applications
        }
        return render(request, "pages/intranet/intranet.html", context)
    
    return redirect('home')
