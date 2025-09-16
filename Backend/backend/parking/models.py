# backend/parking/models.py
from django.db import models
from django.conf import settings


class Parking(models.Model):
    name = models.CharField(max_length=255)  # نام پارکینگ
    address = models.TextField()
    code = models.CharField(max_length=50, unique=True)  # شماره شهرداری یا کد یکتا
    date_joined = models.DateTimeField(auto_now_add=True)  # تاریخ عضویت
    type = models.CharField(
        max_length=20,
        choices=[("شبانه‌روزی", "شبانه‌روزی"), ("روزانه", "روزانه"), ("ساعتی", "ساعتی")],
        default="شبانه‌روزی",
    )
    ev_charge = models.BooleanField(default=False)  # شارژ خودرو برقی
    total_capacity = models.PositiveIntegerField(default=0)

    # مالک پارکینگ - همه فیلدها قابلیت تهی بودن موقت دارند
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    owner_national_id = models.CharField(max_length=20, null=True, blank=True)
    owner_mobile = models.CharField(max_length=11, null=True, blank=True)
    owner_username = models.CharField(max_length=50, null=True, blank=True)
    owner_password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class ParkingSpot(models.Model):
    parking = models.ForeignKey(
        Parking, on_delete=models.CASCADE, related_name="spots", null=True, blank=True
    )
    number = models.CharField(max_length=100)  # شماره جایگاه
    is_occupied = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )
    reserved_at = models.DateTimeField(null=True, blank=True)
    released_at = models.DateTimeField(null=True, blank=True)
    floor = models.IntegerField(default=0)  # اضافه کردن مقدار پیشفرض
    column = models.IntegerField(default=0)  # اضافه کردن مقدار پیشفرض
    row = models.IntegerField(default=0)  # اضافه کردن مقدار پیشفرض
    slot = models.IntegerField(default=0)  # اضافه کردن مقدار پیشفرض

    def __str__(self):
        return f"{self.parking.name} - {self.number}"


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to="qrcodes/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.spot}"
