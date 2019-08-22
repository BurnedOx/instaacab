from django.apps import AppConfig


class RiderConfig(AppConfig):
    name = 'rider'

    def ready(self):
        import rider.signals
