from django.contrib import admin
from .models import ParkingSpot, Reservation


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = [
        "number",
        "is_occupied",
        "reserved_by",
        "reserved_at",
        "released_at",
    ]
    list_filter = ["is_occupied"]
    search_fields = ["number"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "spot", "created_at"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"
