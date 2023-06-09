from django.contrib.postgres.expressions import ArraySubquery
from django.db.models import OuterRef, Prefetch
from django.db.models.functions import JSONObject
from rest_framework.generics import ListAPIView

from apps.address.models import Address
from apps.client.models import Client
from services.api.dashboard.client.serializers.list import ListClientSerializer


class ListClientView(ListAPIView):
    queryset = Client.objects.filter(
        addresses__country__available=True
    ).prefetch_related(
        Prefetch(
            'addresses',
            queryset=Address.objects.select_related('country').only(
                'city', 'street', 'extra', 'country'
            ),
        )
    )
    serializer_class = ListClientSerializer
