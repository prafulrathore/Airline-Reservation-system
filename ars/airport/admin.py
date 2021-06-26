from django.contrib import admin
from airport.models import Airport


@admin.register(Airport)
class Airportadmin(admin.ModelAdmin):
    list_display = ["code", "city"]
