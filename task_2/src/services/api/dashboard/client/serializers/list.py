from rest_framework import serializers

from apps.address.models import Address
from apps.client.models import Client
from apps.country.models import Country


class CountryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        ref_name = 'Country List'
        fields = (
            'id',
            'name',
        )


class AddressClientSerializer(serializers.ModelSerializer):
    country = CountryAddressSerializer(read_only=True)

    class Meta:
        model = Address
        ref_name = 'Address Title List'
        fields = ('city', 'street', 'extra', 'country')


class ListClientSerializer(serializers.ModelSerializer):
    addresses = AddressClientSerializer(read_only=True, many=True)

    class Meta:
        model = Client
        fields = ('name', 'email', 'addresses')
