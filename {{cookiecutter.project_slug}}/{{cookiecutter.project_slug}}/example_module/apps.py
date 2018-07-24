from django.apps import AppConfig


class ExampleModuleConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.example_module'

    def ready(self):
        pass