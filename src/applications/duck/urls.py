from django.urls import path
from django.shortcuts import render

def example_view(request):
    return render(request, "duck/page.html")

urlpatterns = [
    path("", example_view),
]