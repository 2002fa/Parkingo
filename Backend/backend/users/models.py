# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "مدیر سیستم"),
        ("operator", "اپراتور"),
        ("driver", "راننده"),
    )

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="driver", verbose_name="نقش کاربر"
    )
    phone_number = models.CharField(
        max_length=15, blank=True, verbose_name="شماره تلفن"
    )
    license_plate = models.CharField(
        max_length=20, blank=True, verbose_name="پلاک خودرو"
    )

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    def is_admin(self):
        return self.role == "admin"

    def is_operator(self):
        return self.role == "operator"

    def is_driver(self):
        return self.role == "driver"
