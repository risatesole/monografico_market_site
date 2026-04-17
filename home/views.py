from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "name": "My Page",
    }
    return render(request, "pages/home/index.html", context)