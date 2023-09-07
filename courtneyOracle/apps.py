from django.apps import AppConfig

class CourtneyoracleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courtneyOracle'

    def ready(self) -> None:
        from . import signals