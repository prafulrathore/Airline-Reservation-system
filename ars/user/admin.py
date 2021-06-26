from django.contrib import admin

from user.models import Passenger


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "mobile_no",
        "address",
    ]
