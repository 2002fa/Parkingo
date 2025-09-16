# backend/parking/views.py
from rest_framework import viewsets, permissions, status
from .models import Parking, ParkingSpot, Reservation
from .serializers import ParkingSerializer, ParkingSpotSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = request.data
        floors = data.pop("floors", [])

        # --- ساخت یوزر ادمین جدید برای پارکینگ ---
        owner_username = data.get("owner_username")
        owner_password = data.get("owner_password")
        owner_mobile = data.get("owner_mobile")

        if owner_username and owner_password and owner_mobile:
            # بررسی اینکه قبلاً وجود نداشته باشه
            if User.objects.filter(username=owner_username).exists():
                return Response(
                    {"error": "نام کاربری تکراری است."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if User.objects.filter(phone=owner_mobile).exists():
                return Response(
                    {"error": "شماره موبایل تکراری است."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            owner_user = User.objects.create(
                username=owner_username,
                phone=owner_mobile,
                role="admin",
                first_name=data.get("owner_name", ""),
            )
            owner_user.password = make_password(owner_password)
            owner_user.save()
        else:
            owner_user = None

        # --- ساخت پارکینگ ---
        parking_serializer = ParkingSerializer(data=data)
        parking_serializer.is_valid(raise_exception=True)
        parking = parking_serializer.save()

        # (اختیاری) اگر بخوای پارکینگ رو به یوزر وصل کنی:
        # parking.owner_user = owner_user
        # parking.save()

        # --- ساخت جایگاه‌ها ---
        for f_index, floor in enumerate(floors):
            columns = int(floor.get("columns", 1))
            rows = int(floor.get("rows", 1))
            slots = int(floor.get("slots", 1))
            for c in range(1, columns + 1):
                for r in range(1, rows + 1):
                    for s in range(1, slots + 1):
                        ParkingSpot.objects.create(
                            parking=parking,
                            floor=f_index + 1,
                            column=c,
                            row=r,
                            slot=s,
                        )

        return Response(ParkingSerializer(parking).data, status=status.HTTP_201_CREATED)


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
