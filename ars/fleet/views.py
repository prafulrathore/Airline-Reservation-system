from django.shortcuts import render
from rest_framework import generics

from fleet.models import Aircraft, Booking, Flight, Schedule
from fleet.api.serializer import (
    AircraftSerializer,
    FlightSerializer,
    FlightScheduleSerializer,
    BookingInfoSerializer,
)


class AircraftView(generics.ListCreateAPIView):
    """
    POST : Create an Aircraft
    GET : Get a list of all Aircraft
    """

    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AircraftDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET : Get an aircraft
    PUT : Update an aircraft
    DELETE : Delete an aircraft
    """

    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightView(generics.ListCreateAPIView):
    """
    POST : Create an airline
    GET : Get a list of all  the airlines
    """

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET : Get a flight
    PUT : Update a flight
    DELETE : Delete a flight
    """

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightScheduleView(generics.ListCreateAPIView):
    """
    POST : Create a flight schedules
    GET : Get a list of all flight schedules
    """

    queryset = Schedule.objects.all()
    serializer_class = FlightScheduleSerializer


class FlightScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ "
    GET : Get a flight schedules
    PUT : Update a flight schedules
    DELETE : Delete a flight schedules
    """

    queryset = Schedule.objects.all()
    serializer_class = FlightScheduleSerializer


class BookingView(generics.ListCreateAPIView):
    """
    POST : Create a ticket
    GET : Get a list of all tickets
    """

    queryset = Booking.objects.all()
    serializer_class = BookingInfoSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ "
    GET : Get a ticket information of the passenger
    PUT : Update a ticket information of the passenger
    DELETE : Delete a ticket of the passenger
    """

    queryset = Booking.objects.all()
    serializer_class = BookingInfoSerializer


class SearchFlightView(generics.ListAPIView):
    """
    Get : Get a list of those Flights according to search parameter of the url
    """

    serializer_class = FlightSerializer

    def get_queryset(self):
        return Flight.objects.filter()
