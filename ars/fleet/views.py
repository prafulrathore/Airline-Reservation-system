from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

import django_filters
from rest_framework import viewsets
from fleet.models import Aircraft, Booking, Flight, Schedule
from fleet.api.serializer import (
    AircraftSerializer,
    FlightSerializer,
    FlightScheduleSerializer,
    BookingSerializer,
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
    """
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
    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET : Get a ticket information of the passenger
    PUT : Update a ticket information of the passenger
    DELETE : Delete a ticket of the passenger
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class FlightFilter(django_filters.FilterSet):

    from_location = django_filters.CharFilter(
        name="from_location", lookup_type="icontains"
    )
    to_location = django_filters.CharFilter(name="to_location", lookup_type="icontains")

    class Meta:
        model = Flight
        fields = ["from_location", "to_location"]


# class SearchFlight(generics.ListAPIView):
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer
# filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
# # breakpoint()
# ordering_fields = (
#     "from_location",
#     "to_location",
# )
# # ordering = ('last_mod', 'id')
# filter_class = FlightFilter


class SearchFlight(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # filter_backends = [SearchFilter]
    # filter_fields = [
    #     "from_location",
    #     "to_location",
    # ]
    # breakpoint()
    filter_class = FlightFilter




# class SearchFlight(generics.ListAPIView):
#     # lookup_url_kwarg = "start_time", "end_time"
#     serializer_class = FlightSerializer

#     def get_queryset(self):
#         start_time = self.kwargs["start_time"]
#         end_time = self.kwargs["end_time"]
#         breakpoint()
#         qs = Flight.objects.filter(
#             schedule_departure_time__gte=start_time,
#             schedule_departure_time__lte=end_time,
#         )
#         print(qs)
#         return qs

# filter_class = SearchFilter
