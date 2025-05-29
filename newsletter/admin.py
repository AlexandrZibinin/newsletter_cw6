from django.contrib import admin

from newsletter.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("mail_server_answer", "status", "last_send")

