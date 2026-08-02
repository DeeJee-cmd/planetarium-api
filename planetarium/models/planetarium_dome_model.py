from django.db import models


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    seat_in_row = models.IntegerField()

    @property
    def capacity(self):
        return self.row * self.seat_in_row

    class Meta:
        verbose_name_plural = "Planetarium Domes"

    def __str__(self):
        return self.name
