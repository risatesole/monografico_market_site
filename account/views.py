from django.http import HttpResponse

def security(request):
    return HttpResponse("We take security very seriously")

def signIn(request):
    return HttpResponse("Sign In page")

def signUp(request):
    return HttpResponse("sign Up page")

def signOut(request):
    return HttpResponse("Sign Out page")

# Out of project scope:
def validateAccount(request):
    return HttpResponse("validate account view")

def restorePassword(request):
    return HttpResponse("restore password view")

def changeEmail(request):
    return HttpResponse("change email view")
