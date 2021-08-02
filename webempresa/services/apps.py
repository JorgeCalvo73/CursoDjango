from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    # Necesario para traducir la app al castellano
    verbose_name = 'Gestor de servicios'
