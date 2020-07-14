from django.apps import AppConfig


class PatientConfig(AppConfig):
    name = 'patient'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals