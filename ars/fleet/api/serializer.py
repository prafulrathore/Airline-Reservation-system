from rest_framework import serializers

from fleet.models import Aircraft, Flight, Booking


class AircraftSerializer(serializers.ModelSerializer):
    serial_no = serializers.CharField(read_only=True)

    class Meta:
        model = Aircraft
        fields = ["serial_no", "manufacturer", "total_seats"]


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            "aircraft",
            "from_location",
            "to_location",
            "price",
        ]


class FlightScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "flight",
            "departure_date",
            "arrival_date",
            "departure_time",
            "arrival_time",
        ]


class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "passenger_info",
            "flight_schedule",
            "seat",
        ]
