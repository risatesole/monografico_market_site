from .contexts.backoffice_context_handler import backoffice_view_context_handler
from django.shortcuts import render

def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    return render(request, "backoffice/page.html", backoffice_view_context_handler())
