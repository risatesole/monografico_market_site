from django.urls import path
from . import views

urlpatterns = [
    path('provider', views.provider_view, name='provider'),
    path('employee', views.employee_view, name='employee'),
]