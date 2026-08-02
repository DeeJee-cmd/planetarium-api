from django.db import models


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    seat_in_row = models.IntegerField()
