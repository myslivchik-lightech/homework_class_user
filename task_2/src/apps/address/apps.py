from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressConfig(AppConfig):
    name = 'apps.address'
    verbose_name = _('address')
