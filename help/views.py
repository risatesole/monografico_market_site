from django.http import HttpResponse

def help(request):
    return HttpResponse("Welcome to help page")
