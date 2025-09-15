from rest_framework import serializers
from .models import ParkingSpot, Reservation


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    spot_name = serializers.CharField(source="spot.name", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ("user", "qr_code", "is_active")


class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("spot", "start_time", "end_time")
