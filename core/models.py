from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class CustomUserManager(UserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    year_of_entry = models.DateField(null=True, blank=True)
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE, null=True, blank=True)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

