from django.urls import path

from . import views

app_name = "inscriptions"

urlpatterns = [
    path("", views.register, name="register"),
    path("billet/<str:ticket_id>/", views.confirmation, name="confirmation"),
]
