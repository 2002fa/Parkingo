from django.db import models
from django.conf import settings


class ParkingSpot(models.Model):
    number = models.CharField(max_length=10, unique=True)  # شماره جایگاه
    is_occupied = models.BooleanField(default=False)  # پر یا خالی
    reserved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )
    reserved_at = models.DateTimeField(null=True, blank=True)
    released_at = models.DateTimeField(null=True, blank=True)


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to="qrcodes/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
