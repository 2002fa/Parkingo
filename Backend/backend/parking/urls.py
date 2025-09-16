# backend/parking/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingViewSet, ParkingSpotViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r"parkings", ParkingViewSet, basename="parking")
router.register(r"parking-spots", ParkingSpotViewSet, basename="parking-spot")
router.register(r"reservations", ReservationViewSet, basename="reservation")

urlpatterns = [
    path("", include(router.urls)),
]