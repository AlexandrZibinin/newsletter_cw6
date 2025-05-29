from django.core.management import BaseCommand

from newsletter.services import newsletter_send_email


class Command(BaseCommand):

    def handle(self, *args, **options):
        newsletter_send_email()
        return f"Рассылка запущена"
