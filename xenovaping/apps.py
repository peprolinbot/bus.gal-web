from django.apps import AppConfig


class XenovapingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xenovaping'

    def ready(self):
        from .tasks import setup_tasks
        setup_tasks()
        
