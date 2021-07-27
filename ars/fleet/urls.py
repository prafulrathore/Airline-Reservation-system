from django.urls import path

from fleet import views

urlpatterns = [
    path(
        "aircraft/",
        views.AircraftView.as_view(),
        name="aircraft-create-list",
    ),
    path(
        "aircraft/<int:pk>/",
        views.AircraftDetailView.as_view(),
        name="aircraft-rud",
    ),
    path("flight/", views.FlightView.as_view(), name="flight-list-create"),
    path(
        "flight/<int:pk>/",
        views.FlightDetailView.as_view(),
        name="flight-rud",
    ),
    path(
        "schedule/",
        views.FlightScheduleView.as_view(),
        name="Flight-schedule-list-create",
    ),
    path(
        "schedule/<int:pk>/",
        views.FlightScheduleDetailView.as_view(),
        name="flight-schedule-rud",
    ),
    path("booking/", views.BookingView.as_view(), name="booking-list-create"),
    path(
        "booking/<int:pk>/",
        views.BookingDetailView.as_view(),
        name="Booking-rud",
    ),
    path(
        "search",
        views.SearchFlight.as_view(),
        name="search-flight",
    ),
]
