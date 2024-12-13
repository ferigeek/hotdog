from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class Admin(UserAdmin):
    model = models.User
    list_display = ['email', 'is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email', 'first_name', 'last_name']


admin.site.register(models.User, Admin)
admin.site.register(models.FieldOfStudy)
