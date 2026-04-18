from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')


admin.site.register(User, UserAdmin)