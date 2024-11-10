from django.apps import AppConfig


class ShorturlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shorturl'
    verbose_name = 'Shorten URLs'
    description = 'A simple URL shortening service'

