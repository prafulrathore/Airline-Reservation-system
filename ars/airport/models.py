from django.db import models


class Airport(models.Model):
    code = models.CharField(
        max_length=4, null=True, blank=True, verbose_name="Airport Code"
    )
    city = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Airport Cities"
    )
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.code}-{self.city}"
