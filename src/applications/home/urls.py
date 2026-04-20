from django.urls import path
from .views import home 
from .views import signin_view
from .views import signout_view
from .views import signup_view
from .views import settings_view
from .views import provider_view
from .views import provider_request_view
from .views import internal_view

urlpatterns = [
    path("", home, name="home"),

    # authentication
    path("signin/", signin_view, name="signin"),
    path("signout/", signout_view, name="signout"),
    path("signup/", signup_view, name="signup"),

    # user settings
    # path('settings/', settings_view, name='settings_page'),

    # provider
    path("provider/request/", provider_request_view, name="provider_request"),
    path("provider/", provider_view, name="provider"),

    # internal views
    path("internal/", internal_view, name="internal")
]
