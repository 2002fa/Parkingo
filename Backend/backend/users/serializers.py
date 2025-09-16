from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "phone", "role", "first_name", "last_name")


class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email_or_username = data.get("email_or_username")
        phone = data.get("phone")
        password = data.get("password")

        # بررسی وجود کاربر با ایمیل/نام کاربری و شماره تلفن
        try:
            if "@" in email_or_username:
                user = User.objects.get(email=email_or_username, phone=phone)
            else:
                user = User.objects.get(username=email_or_username, phone=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError("کاربری با این مشخصات یافت نشد")

        # بررسی صحت رمز عبور
        if not user.check_password(password):
            raise serializers.ValidationError("رمز عبور اشتباه است")

        if not user.is_active:
            raise serializers.ValidationError("حساب کاربری غیرفعال است")

        data["user"] = user
        return data


class OTPSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
    phone = serializers.CharField()
