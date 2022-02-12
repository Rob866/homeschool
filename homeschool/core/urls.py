from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("app/", views.app, name="app"),
]
