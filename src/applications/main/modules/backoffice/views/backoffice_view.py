from .contexts.backoffice_context_handler import backoffice_view_context_handler
from django.shortcuts import render
from .form_actions.handler import form_actions_handler

def backoffice_view(request):
    """HANDLE POST ACTIONS"""
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type:
            """FORM ACTIONS/HANDLERS"""
            form_actions_handler(request, form_type)

    return render(request, "backoffice/page.html", backoffice_view_context_handler())
