from django.contrib import admin

from client.models import Client


@admin.register(Client)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("email", "owner",)
