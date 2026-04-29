from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def preferences_user_view(request):
    user = request.user

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        # Handle password change safely
        password = request.POST.get("password")
        if password:
            user.set_password(password)
            update_session_auth_hash(request, user)  # keeps user logged in

        user.save()
        return redirect("preferences")

    return render(request, "user/preferences.html")
