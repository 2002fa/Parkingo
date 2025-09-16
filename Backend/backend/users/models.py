from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("driver", "راننده"),
        ("operator", "اپراتور"),
        ("admin", "مدیر"),
    )

    phone = models.CharField(
        max_length=15, unique=True, verbose_name="شماره تلفن"
    )

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="driver", verbose_name="نقش"
    )

    # فیلدهای اضافی اگر نیاز دارید
    # profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
