from django.urls import path
from .views import home , dashboard, signin_view, signout_view, signup_view, settings_view, provider_view, apply_to_be_provider_view, provider_request_view

urlpatterns = [
    path("", home, name="home"),

    # intranet site
    path("dashboard/", dashboard, name="dashboard"),

    # authentication
    path("signin/", signin_view, name="signin"),
    path("signout/", signout_view, name="signout"),
    path("signup/", signup_view, name="signup"),

    # user settings
    path('settings/', settings_view, name='settings_page'),

    # provider
    path("provider/request/", provider_request_view, name="provider_request"),
    path("provider/", provider_view, name="provider")
]
