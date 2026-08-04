from django.db import models
from rest_framework.exceptions import ValidationError

from .show_session_model import ShowSession
from .reservation_model import Reservation



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

    @staticmethod
    def validate_seat(row, seat, planetarium_dome, error_to_raise):
        for ticket_attr_value, dome_attr_name, error_name in [
            (row, "row", "row"),
            (seat, "seat_in_row", "seat"),
        ]:
            count_attrs = getattr(planetarium_dome, dome_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        error_name: f"{error_name} must be in range "
                                    f"[1, {count_attrs}], not {ticket_attr_value}"
                    }
                )

    def clean(self):
        Ticket.validate_seat(
            self.row,
            self.seat,
            self.show_session.planetarium_dome,
            ValidationError,
        )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"row: {self.row} - seat: {self.seat}"
