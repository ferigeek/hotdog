from django.db import models
from django.contrib.auth.models import AbstractUser


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    year_of_entry = models.DateField()
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'field_of_study']


