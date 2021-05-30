from django.apps import AppConfig


class UserssConfig(AppConfig):
    name = 'userss'

    def ready(self):
        import userss.signals
