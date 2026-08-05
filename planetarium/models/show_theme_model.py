from django.db import models


class ShowTheme(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Show Theme"

    def __str__(self):
        return self.name
