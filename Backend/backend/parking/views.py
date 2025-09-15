from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import ParkingSpot, Reservation
from .serializers import (
    ParkingSpotSerializer,
    ReservationSerializer,
    ReservationCreateSerializer,
)


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [permissions.AllowAny]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()  # این خط را اضافه کنید
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # فیلتر کردن بر اساس کاربر لاگین شده
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"], permission_classes=[permissions.AllowAny])
    def available_spots(self, request):
        now = timezone.now()
        occupied_spots = Reservation.objects.filter(
            start_time__lte=now, end_time__gte=now, is_active=True
        ).values_list("spot_id", flat=True)

        available_spots = ParkingSpot.objects.exclude(id__in=occupied_spots)
        serializer = ParkingSpotSerializer(available_spots, many=True)
        return Response(serializer.data)
