from django.db import models


class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Astronomy Shows"

    def __str__(self):
        return self.title
