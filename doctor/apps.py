from django.apps import AppConfig


class DoctorConfig(AppConfig):
    name = 'doctor'

    def ready(self):
        import social.mysignal
