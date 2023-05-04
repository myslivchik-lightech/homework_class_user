from django.urls import path, include

from services.api.dashboard.client.urls import urlpatterns as client_urls

app_name = 'dashboard'

urlpatterns = [
    path(
        'client/',
        include((client_urls, 'client'), namespace='client'),
    ),
]
