from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from user.models import Passenger
from user.api.serializer import PassengerSerializer
from django.contrib.auth.models import User


class PassengerCreateView(generics.CreateAPIView):
    """
    POST : create a passenger
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    def create(self, request, *args, **kwargs):
        serializer = PassengerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassengerListView(generics.ListAPIView):
    """
    Get : Get a list of all the passengers
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET : Get a passenger details
    PUT : Update a passenger details
    DELETE : Delete a passenger details
    """

    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
