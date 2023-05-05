from django.db import models


class Address(models.Model):
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
        related_name='address',
    )
    country = models.ForeignKey(
        'country.Country',
        on_delete=models.CASCADE,
        related_name='address',
    )
    city = models.CharField()
    street = models.CharField()
    extra = models.CharField(help_text="дом, квартира, подъезд")
    zip_code = models.CharField()
