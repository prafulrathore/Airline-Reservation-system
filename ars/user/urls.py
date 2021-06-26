from django.urls import path

from user import views

urlpatterns = [
    path("create/", views.PassengerCreateView.as_view(), name="passenger-create"),
    path("list/", views.PassengerListView.as_view(), name="passenger-list"),
    path(
        "detail-update-delete/<int:pk>",
        views.PassengerDetailView.as_view(),
        name="passenger-detail-update-delete",
    ),
]
