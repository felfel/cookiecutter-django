from django.urls import path

from .views import ExampleView
# Set up your routes here

app_name = '{{cookiecutter.project_slug}}.example_module'

urlpatterns = [
    path(
        "hello-world/",
        ExampleView.as_view(),
        name="hello-world",
    )
]