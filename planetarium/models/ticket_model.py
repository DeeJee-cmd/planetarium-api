from django.db import models


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()

    class Meta:
        unique_together = ("row", "seat"),
        ordering = ("seat",)

    def __str__(self):
        return f"row: {self.row} - seat: {self.seat}"
