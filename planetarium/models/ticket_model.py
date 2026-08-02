from django.db import models
from planetarium.models import (
    ShowSession,
    Reservation,
)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(
        ShowSession,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="tickets",
    )

    class Meta:
        unique_together = ("show_session", "row", "seat")
        ordering = ("row", "seat")

    def __str__(self):
        return f"row: {self.row} - seat: {self.seat}"
