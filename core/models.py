from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class HotdogUser(AbstractUser):
    username = models.IntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'field_of_study']
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

class Course(models.Model):
    course_name = models.CharField(max_length=255, blank=True, null=True)
    instructor = models.CharField(max_length=255, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def clean_year(self):
        pass

    def __str__(self):
        return f"{self.course_name} - {self.semester} {self.year}"