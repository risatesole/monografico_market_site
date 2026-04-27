from .modules.views.web.view_web_signup import signup_view

def duck(request):
    return signup_view(request)
