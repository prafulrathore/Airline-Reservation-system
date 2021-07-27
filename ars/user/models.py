from django.db import models

from django.contrib.auth.models import User

AGE_CHOICES = (("Children", "Children"), ("Adult", "Adult"))


class Passenger(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.CharField(default=0, choices=AGE_CHOICES, max_length=10)
    mobile_no = models.CharField(max_length=10, verbose_name="contact_no")
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.customer}"
