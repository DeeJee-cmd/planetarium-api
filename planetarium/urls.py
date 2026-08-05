from rest_framework import routers
from django.urls import path, include

from .views import (
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    AstronomyShowViewSet,
    ShowSessionViewSet,
    TicketViewSet,
    ReservationViewSet,
)

router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("tickets", TicketViewSet)
router.register("reservations", ReservationViewSet, basename="reservation")

urlpatterns = [path("", include(router.urls))]

app_name = "planetarium"
