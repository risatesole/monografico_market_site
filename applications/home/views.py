from django.http import HttpResponse
from django.shortcuts import render
from utils.env import environment

def home(request):
    context = {
        "name": environment["name"],
    }
    return render(request, "pages/home/index.html", context)