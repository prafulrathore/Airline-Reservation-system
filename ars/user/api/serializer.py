from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Passenger


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class PassengerSerializer(serializers.ModelSerializer):
    customer = UserSerializer()

    class Meta:
        model = Passenger
        fields = ["customer", "age", "mobile_no", "address"]

    def create(self, validated_data):
        # Create the passenger instance with the user instance
        customer = validated_data.pop("customer")
        passenger = Passenger.objects.create(**validated_data)
        new_customer = User.objects.create(**customer)
        passenger.customer = new_customer
        passenger.save()
        return passenger

    def update(self, instance, validated_data):
        # Update the passenger instance
        user = self.fields["customer"]
        nested_instance = instance.customer
        customer_data = validated_data.pop("customer")
        instance.age = validated_data["age"]
        instance.mobile_no = validated_data["mobile_no"]
        instance.address = validated_data["address"]
        instance.save()
        user.update(nested_instance, customer_data)
        return super(PassengerSerializer, self).update(instance, validated_data)
