from django.apps import AppConfig


class ShehitaaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shehitaa'

    def ready(self) -> None:
        import shehitaa.signals