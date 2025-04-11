from django.contrib import admin
from . import models

admin.site.register(models.HotdogUser)
admin.site.register(models.Course)
admin.site.register(models.FieldOfStudy)