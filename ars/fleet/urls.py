from django.urls import path

from fleet import views

urlpatterns = [
    path(
        "aircraft/list/create/",
        views.AircraftView.as_view(),
        name="aircraft-create-list",
    ),
    path(
        "aircraft/detail-update-delete/<int:pk>/",
        views.AircraftDetailView.as_view(),
        name="aircraft-detail-update-delete",
    ),
    path("flight/list/create/", views.FlightView.as_view(), name="flight-create"),
    path(
        "flight/detail-update-delete/<int:pk>/",
        views.FlightDetailView.as_view(),
        name="flight-detail",
    ),
    path(
        "schedule/list/create/",
        views.FlightScheduleView.as_view(),
        name="Flight-schedule-list-create",
    ),
    path(
        "shedule/detail-update-delete/<int:pk>/",
        views.FlightScheduleDetailView.as_view(),
        name="flight-schedule-detail",
    ),
    path(
        "booking/list/create/", views.BookingView.as_view(), name="booking-list-create"
    ),
    path(
        "booking/detail-update-delete/<int:pk>/",
        views.BookingDetailView.as_view(),
        name="Booking-detail",
    ),
]
