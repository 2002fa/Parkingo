# backend/parking/views.py
from rest_framework import viewsets, permissions, status
from .models import Parking, ParkingSpot, Reservation
from .serializers import ParkingSerializer, ParkingSpotSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = [IsAdminUser]  # فقط لاگین کرده‌ها ببینن

    def create(self, request, *args, **kwargs):
        data = request.data
        floors = data.pop("floors", [])

        # ثبت پارکینگ
        parking_serializer = ParkingSerializer(data=data)
        parking_serializer.is_valid(raise_exception=True)
        parking = parking_serializer.save()

        # ساخت جایگاه‌ها طبق طبقات
        for f_index, floor in enumerate(floors):
            columns = int(floor.get("columns", 1))
            rows = int(floor.get("rows", 1))
            slots = int(floor.get("slots", 1))
            for c in range(1, columns + 1):
                for r in range(1, rows + 1):
                    for s in range(1, slots + 1):
                        ParkingSpot.objects.create(
                            parking=parking, floor=f_index + 1, column=c, row=r, slot=s
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
