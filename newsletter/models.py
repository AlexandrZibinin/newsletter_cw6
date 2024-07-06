from django.db import models

PERIOD_SEND_CHOICES = {
    "day": "Раз в день",
    "week": "Раз в неделю",
    "month": "Раз в месяц",
}


class Newsletter(models.Model):
    first_send = models.DateTimeField(
        auto_now=False, auto_now_add=False, verbose_name="дата и время первой отправки"
    )
    period = models.CharField(
        max_length=10, choices=PERIOD_SEND_CHOICES, verbose_name="период отправки"
    )
    status = models.BooleanField(verbose_name="статус отправки")
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




