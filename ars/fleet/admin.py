from django.contrib import admin

from fleet.models import Aircraft, Flight, Schedule, Booking

# Register your models here.
@admin.register(Aircraft)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ["manufacturer", "serial_no"]


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["aircraft", "from_location", "to_location", "price"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "flight",
        "departure_date",
        "arrival_date",
        "departure_time",
        "arrival_time",
    ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["passenger_info", "flight_schedule", "seat"]
