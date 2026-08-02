from rest_framework import serializers

from planetarium.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "show_session", "reservation")

    def validate(self, attrs):
        data = super().validate(attrs)
        Ticket.validate_seat(
            attrs["row"],
            attrs["seat"],
            attrs["show_session"].planetarium_dome,
            serializers.ValidationError,
        )
        return data


class TicketListSerializer(TicketSerializer):
    class Meta(TicketSerializer.Meta):
        fields = ("id", "row", "seat")
