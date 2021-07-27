from pyexpat import model
from rest_framework import serializers

from airport.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    airport = serializers.StringRelatedField()

    class Meta:
        model = Airport
        fleids = ["id", "code", "city"]
