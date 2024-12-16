from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy
from . import models


class Admin(UserAdmin):
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name', 'year_of_entry', 'field_of_study']
    list_filter = ['is_staff', 'is_superuser', 'field_of_study']
    search_fields = ['email', 'first_name', 'last_name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (gettext_lazy('Personal Info'), {'fields': ('first_name', 'last_name', 'year_of_entry', 'field_of_study')}),
        (gettext_lazy('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (gettext_lazy('Important Dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )


admin.site.register(models.User, Admin)
admin.site.register(models.FieldOfStudy)
