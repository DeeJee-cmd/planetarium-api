from rest_framework import serializers

from planetarium.models.show_session_model import ShowSession
from planetarium.serializers import AstronomyShowDetailSerializer, PlanetariumDomeSerializer


class ShowSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetarium_dome", "show_time")


class ShowSessionListSerializer(ShowSessionSerializer):
    astronomy_show_title = serializers.CharField(
        source="astronomy_show.title", read_only=True
    )
    planetarium_dome_name = serializers.CharField(
        source="planetarium_dome.name", read_only=True
    )
    planetarium_dome_capacity = serializers.IntegerField(
        source="planetarium_dome.capacity", read_only=True
    )

    class Meta:
        model = ShowSession
        fields = (
            "id",
            "astronomy_show_title",
            "planetarium_dome_name",
            "planetarium_dome_capacity",
            "show_time",
        )


class ShowSessionDetailSerializer(ShowSessionSerializer):
    """Щоб не виникав цикл"""

    # from .astronomy_show_serializer import AstronomyShowDetailSerializer
    # from .planetarium_dome_serializer import PlanetariumDomeSerializer
    astronomy_show = AstronomyShowDetailSerializer(read_only=True)
    planetarium_dome = PlanetariumDomeSerializer(read_only=True)
