from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "role", "is_staff"]
    list_filter = ["role", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("اطلاعات اضافی", {"fields": ("role", "phone_number", "license_plate")}),
    )
