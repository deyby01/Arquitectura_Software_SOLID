from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Este metodo se ejecuta una vez que Django esta listo.
        # Es el lugar perfecto para inicializar nuestro contenedor.
        from . import containers

        # Simplemente creamos la instancia.
        # El contenedor se configurara a si mismo gracias al wiring_config.
        container = containers.Container()
