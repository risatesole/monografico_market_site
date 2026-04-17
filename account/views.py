from django.http import HttpResponse

def security(request):
    return HttpResponse("We take security very seriously")
