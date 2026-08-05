from rest_framework import viewsets

from planetarium.models import ShowSession
from planetarium.serializers import (
    ShowSessionSerializer,
    ShowSessionListSerializer,
    ShowSessionDetailSerializer,
)


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.select_related("astronomy_show", "planetarium_dome")
    serializer_class = ShowSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShowSessionListSerializer
        if self.action == "retrieve":
            return ShowSessionDetailSerializer
        return ShowSessionSerializer
