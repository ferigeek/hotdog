from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class HotdogUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'field_of_study']
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Course(models.Model):
    course_name = models.CharField(max_length=255, blank=True, null=True)
    instructor = models.CharField(max_length=255, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def clean(self):
        if self.semester < 1 or self.semester > 2:
            raise ValueError("Semester must be either 1 or 2.")
        if self.year < (datetime.now().year - 1) or self.year > (datetime.now().year + 1):
            raise ValueError("Invalid year.")

    def __str__(self):
        return f"{self.course_name} - {self.semester} {self.year}"