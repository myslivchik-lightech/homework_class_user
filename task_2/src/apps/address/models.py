from django.db import models


class Address(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    country = models.ForeignKey('country.Country', on_delete=models.CASCADE)
    city = models.CharField()
    street = models.CharField()
    extra = models.CharField(help_text="дом, квартира, подъезд")
    zip_code = models.CharField()
