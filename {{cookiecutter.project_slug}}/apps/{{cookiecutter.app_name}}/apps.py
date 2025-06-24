from django.apps import AppConfig


class {{cookiecutter.app_name.title()}}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{{cookiecutter.app_name}}'