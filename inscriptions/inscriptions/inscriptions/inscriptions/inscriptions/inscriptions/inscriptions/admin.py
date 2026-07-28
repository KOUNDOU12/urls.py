from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "ticket_id",
        "nom",
        "categorie",
        "ville",
        "place",
        "date_inscription",
    )
    list_filter = ("categorie", "ville")
    search_fields = ("nom", "email", "telephone", "ticket_id")
    readonly_fields = ("ticket_id", "place", "date_inscription")
