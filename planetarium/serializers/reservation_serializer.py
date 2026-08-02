from django.db import transaction
from rest_framework import serializers

from planetarium.models import Reservation, Ticket
from planetarium.serializers.ticket_serializer import TicketSerializer


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "tickets")

    def create(self, validated_data):
        tickets_data = validated_data.pop("tickets")
        with transaction.atomic():
            reservation = Reservation.objects.create(
                user=self.context["request"].user, **validated_data
            )
            for ticket_data in tickets_data:
                Ticket.objects.create(reservation=reservation, **ticket_data)
        return reservation
