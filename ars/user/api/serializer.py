from rest_framework import serializers

from user.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()

    class Meta:
        model = Passenger
        fields = ["customer", "age", "mobile_no", "address"]
