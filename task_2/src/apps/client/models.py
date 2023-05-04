from django.db import models


class Client(models.Model):
    name = models.CharField()
    email = models.CharField()
