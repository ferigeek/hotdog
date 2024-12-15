from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class Admin(UserAdmin):
    model = models.User
    list_display = ('email', 'first_name', 'last_name', 'year_of_entry', 'field_of_study', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'field_of_study')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'year_of_entry', 'field_of_study')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'year_of_entry', 'field_of_study', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(models.User, Admin)
admin.site.register(models.FieldOfStudy)
