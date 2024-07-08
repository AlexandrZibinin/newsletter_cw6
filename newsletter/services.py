import smtplib
from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail

from config import settings
from newsletter.models import Newsletter, Mailing


def newsletter_send_email():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    mailings = Newsletter.objects.all().filter(status="on").filter(first_send__lte=current_datetime)


    for mailing in mailings:
        try:
            mail_response = send_mail(
                subject=mailing.message.title,
                message=mailing.message.text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client.all()],
                fail_silently=False
            )
            print(mail_response)
            mailing_send = Mailing.objects.create(mailing=mailing, status="done")
            if mailing.period == "day":
                mailing.first_send = current_datetime + timedelta(days=1)
            elif mailing.period == "week":
                mailing.first_send = current_datetime + timedelta(days=7)
            elif mailing.period == "month":
                mailing.first_send = current_datetime + timedelta(day=30)

        except smtplib.SMTPException as e:
            mailing_send = Mailing.objects.create(mailing=mailing, status="error", mail_server_answer=e)


        mailing.save()
        mailing_send.save()
