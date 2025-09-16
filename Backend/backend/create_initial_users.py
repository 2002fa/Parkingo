import os
import django
import sys

# اضافه کردن مسیر پروژه به sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from users.models import User


def create_initial_users():
    # ایجاد کاربر ادمین
    admin_user, created = User.objects.get_or_create(
        username="admin",
        defaults={
            "email": "admin@parkingo.com",
            "phone": "09123456789",
            "role": "admin",
            "is_staff": True,
            "is_superuser": True,
            "first_name": "مدیر",
            "last_name": "سیستم",
        },
    )
    if created:
        admin_user.set_password("admin123")
        admin_user.save()
        print("✅ کاربر ادمین ایجاد شد")
    else:
        print("⚠️ کاربر ادمین از قبل وجود داشت")

    # ایجاد کاربر اپراتور
    operator_user, created = User.objects.get_or_create(
        username="operator",
        defaults={
            "email": "operator@parkingo.com",
            "phone": "09123456780",
            "role": "operator",
            "is_staff": True,
            "first_name": "اپراتور",
            "last_name": "سیستم",
        },
    )
    if created:
        operator_user.set_password("operator123")
        operator_user.save()
        print("✅ کاربر اپراتور ایجاد شد")
    else:
        print("⚠️ کاربر اپراتور از قبل وجود داشت")

    # ایجاد کاربر راننده نمونه
    driver_user, created = User.objects.get_or_create(
        username="driver1",
        defaults={
            "email": "driver1@example.com",
            "phone": "09123456781",
            "role": "driver",
            "first_name": "راننده",
            "last_name": "نمونه",
        },
    )
    if created:
        driver_user.set_password("driver123")
        driver_user.save()
        print(" کاربر راننده ایجاد شد")
    else:
        print(" کاربر راننده از قبل وجود داشت")


if __name__ == "__main__":
    create_initial_users()
    print(" ایجاد کاربران اولیه завер شد!")
