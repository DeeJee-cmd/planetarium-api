from rest_framework import viewsets

from planetarium.models import Ticket
from planetarium.serializers import TicketSerializer, TicketListSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TicketListSerializer
        return TicketSerializer
