from django.db import models

PERIOD_SEND_CHOICES = {
    "day": "Раз в день",
    "week": "Раз в неделю",
    "month": "Раз в месяц",
}

STATUS_SEND_CHOICES = {
    "off": "Отключена",
    "on": "Включена",
}

STATUS_MAILING_CHOICE = {
    "done": "Успех",
    "error": "Ошибка",
}

NULLABLE = {"blank": True, "null": True}


class Newsletter(models.Model):
    first_send = models.DateTimeField(
        auto_now=False, auto_now_add=False, verbose_name="дата и время первой отправки"
    )
    period = models.CharField(
        max_length=10, choices=PERIOD_SEND_CHOICES, verbose_name="период отправки"
    )
    status = models.CharField(
        choices=STATUS_SEND_CHOICES, default="off", verbose_name="статус отправки"
    )
    client = models.ManyToManyField("client.Client", verbose_name="получатель")
    message = models.ForeignKey(
        "letter.Letter",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="сообщение",
    )


    def __str__(self):
        return f"{self.first_send}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Mailing(models.Model):
    last_send = models.DateTimeField(
        auto_now_add=True, verbose_name="дата и время последней отправки"
    )
    status = models.CharField(choices=STATUS_MAILING_CHOICE, verbose_name="статус отправки")
    mail_server_answer = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Ответ SMPT сервера"
    )
    mailing = models.ForeignKey("Newsletter", verbose_name="попытка рассылки", on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.last_send}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"

