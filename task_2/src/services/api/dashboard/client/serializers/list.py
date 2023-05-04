from rest_framework import serializers

from apps.client.models import Client


class ListClientSerializer(serializers.ModelSerializer):
    addresses = serializers.JSONField(read_only=True)

    class Meta:
        model = Client
        fields = ('name', 'email', 'addresses')
