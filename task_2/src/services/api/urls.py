from django.urls import include, path


app_name = 'api'

urlpatterns = [
    path('dashboard/', include('services.api.dashboard.urls')),
]
