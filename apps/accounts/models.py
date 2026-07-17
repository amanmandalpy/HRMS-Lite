from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.accounts.managers import CustomUserManager
from apps.accounts.choices import UserRole
from apps.common.models import BaseModel

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.EMPLOYEE,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email
