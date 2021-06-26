from tabnanny import verbose
import uuid

from django.db import models

from airport.models import Airport
from user.models import Passenger


class Aircraft(models.Model):
    serial_no = models.CharField(
        max_length=6, primary_key=True, editable=False, default=135452
    )
    manufacturer = models.CharField(max_length=100)
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.manufacturer}"

    def save(self, *args, **kwargs):
        self.serial_no = uuid.uuid4().hex[:6].upper()
        super(Aircraft, self).save(*args, **kwargs)


class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    from_location = models.ForeignKey(
        Airport,
        null=True,
        blank=True,
        related_name="flight_in",
        on_delete=models.CASCADE,
    )
    to_location = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="flight_out",
    )
    price = models.IntegerField()

    def __str__(self):
        return f"{self.aircraft}"


class Schedule(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()

    class Meta:
        verbose_name = "Flight Schedule"
        verbose_name_plural = "Flight Schedules"

    def __str__(self):
        return f"{self.departure_date}-{self.arrival_date}"


class Booking(models.Model):
    passenger_info = models.ForeignKey(
        Passenger, on_delete=models.CASCADE, verbose_name="passenger"
    )
    flight_schedule = models.ForeignKey(
        Flight, on_delete=models.CASCADE, verbose_name="schedule"
    )
    seat = models.IntegerField()

    def __str__(self):
        return f"Booking details of {self.passenger}"
