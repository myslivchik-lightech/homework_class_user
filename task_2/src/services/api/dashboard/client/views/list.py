from django.contrib.postgres.expressions import ArraySubquery
from django.db.models import OuterRef
from django.db.models.functions import JSONObject
from rest_framework.generics import ListAPIView

from apps.address.models import Address
from apps.client.models import Client
from services.api.dashboard.client.serializers.list import ListClientSerializer


class ListClientView(ListAPIView):
    queryset = Client.objects.filter(
        address__country__available=True
    ).annotate(
        addresses=ArraySubquery(
            Address.objects.annotate(
                sub_address=JSONObject(
                    country=JSONObject(id='country_id', name='country__name'),
                    city='city',
                    street='street',
                    extra='extra',
                )
            )
            .filter(client=OuterRef('id'), country__available=True)
            .values('sub_address')
        )
    )
    serializer_class = ListClientSerializer
