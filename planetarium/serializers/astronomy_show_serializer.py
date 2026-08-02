from rest_framework import serializers

from planetarium.models import AstronomyShow
from planetarium.serializers.show_theme_serializer import ShowThemeSerializer


class AstronomyShowSerializer(serializers.Serializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_theme")


class AstronomyShowListSerializer(AstronomyShowSerializer):
    show_theme = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )


class AstronomyShowDetailSerializer(AstronomyShowSerializer):
    show_theme = ShowThemeSerializer(many=True, read_only=True)
