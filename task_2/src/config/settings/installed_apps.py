INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'apps.address.apps.AddressConfig',
    'apps.client.apps.ClientConfig',
    'apps.country.apps.CountryConfig',
]