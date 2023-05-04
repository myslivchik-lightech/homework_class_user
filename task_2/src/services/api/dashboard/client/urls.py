from django.urls import path

from services.api.dashboard.client.views.list import ListClientView

app_name = 'client'

urlpatterns = [
    path('list/', ListClientView.as_view(), name='list'),
]
