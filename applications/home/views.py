from django.http import HttpResponse
from django.shortcuts import render
from utils.env import environment

context = {
    "name": environment["name"],
}

def home(request): return render(request, "pages/home/index.html", context)
