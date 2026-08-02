from django.db import models

from planetarium.models import ShowTheme


class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    show_theme = models.ManyToManyField(
        ShowTheme,
        related_name="astronomy_shows"
    )

    class Meta:
        verbose_name_plural = "Astronomy Shows"

    def __str__(self):
        return self.title
