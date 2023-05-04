from django.db import models


class Country(models.Model):
    name = models.CharField()
    available = models.BooleanField()
