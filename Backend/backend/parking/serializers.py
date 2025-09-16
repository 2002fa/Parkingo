# backend/parking/serializers.py
from rest_framework import serializers
from .models import Parking, ParkingSpot, Reservation

# class ParkingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Parking
#         fields = "__all__"


class ParkingSpotSerializer(serializers.ModelSerializer):
    parking_name = serializers.CharField(source="parking.name", read_only=True)

    class Meta:
        model = ParkingSpot
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    spot_name = serializers.CharField(source="spot.number", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ("user", "qr_code")

class ParkingSerializer(serializers.ModelSerializer):
    spots = ParkingSpotSerializer(many=True, read_only=True)
    class Meta:
        model = Parking
        fields = "__all__"
