from rest_framework import serializers

from planetarium.models import PlanetariumDome


class PlanetariumDomeSerializer(serializers.Serializer):
    class Meta:
        model = PlanetariumDome
        fields = (
            "id",
            "name",
            "row",
            "seat_in_row",
            "capacity",
        )


class PlanetariumDomeListSerializer(PlanetariumDomeSerializer):
    class Meta(PlanetariumDomeSerializer.Meta):
        fields = ("id", "name", "capacity")
