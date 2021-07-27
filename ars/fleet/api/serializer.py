from rest_framework import serializers

from fleet.models import Aircraft, Flight, Booking, Schedule
from airport.models import Airport
from user.models import Passenger
from airport.api.serializers import AirportSerializer
from user.api.serializer import PassengerSerializer

from django.contrib.auth.models import User


class AircraftSerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(read_only=True)

    class Meta:
        model = Aircraft
        fields = ["serial_no", "manufacturer", "total_seats"]


class FlightSerializer(serializers.ModelSerializer):
    from_location = serializers.SlugRelatedField(
        queryset=Airport.objects.all(), slug_field="code"
    )
    to_location = serializers.SlugRelatedField(
        queryset=Airport.objects.all(), slug_field="code"
    )

    class Meta:
        model = Flight
        fields = [
            "id",
            "aircraft",
            "from_location",
            "to_location",
            "price",
        ]


class FlightScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "flight",
            "departure_date",
            "arrival_date",
            "departure_time",
            "arrival_time",
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "passenger_info",
            "flight_schedule",
            "seat",
        ]
