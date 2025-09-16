from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
import random
from .serializers import LoginSerializer, OTPSerializer, UserSerializer
from .models import User
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            # تولید کد OTP (در محیط واقعی باید از سرویس SMS استفاده کنید)
            otp_code = str(random.randint(1000, 9999))

            # ذخیره OTP در کش به مدت 5 دقیقه
            cache.set(f"otp_{user.phone}", otp_code, timeout=300)

            # در اینجا باید کد ارسال به تلفن کاربر را پیاده سازی کنید
            # send_sms(user.phone, f'کد تأیید شما: {otp_code}')

            print(f"کد OTP برای {user.phone}: {otp_code}")  # فقط برای توسعه

            return Response(
                {
                    "message": "کد تأیید ارسال شد",
                    "phone": user.phone,
                    "user_id": user.id,
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            code = serializer.validated_data["code"]

            # بررسی صحت کد OTP
            cached_code = cache.get(f"otp_{phone}")

            if cached_code and cached_code == code:
                # پیدا کردن کاربر
                try:
                    user = User.objects.get(phone=phone)
                except User.DoesNotExist:
                    return Response(
                        {"error": "کاربر یافت نشد"}, status=status.HTTP_404_NOT_FOUND
                    )

                # ایجاد توکن (در حالت واقعی از JWT یا Simple JWT استفاده کنید)
                from rest_framework.authtoken.models import Token

                token, created = Token.objects.get_or_create(user=user)

                # پاک کردن کد استفاده شده از کش
                cache.delete(f"otp_{phone}")

                return Response(
                    {"token": token.key, "user": UserSerializer(user).data},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "کد تأیید نامعتبر است"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
