from split_settings.tools import include, optional

include(
    'base.py',
    'installed_apps.py',
    'database.py',
    'storage.py',
    optional('local_settings.py'),
)
