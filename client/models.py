from django.db import models


class Client(models.Model):
    full_name = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="ФИО"
    )
    email = models.EmailField(
        max_length=100, blank=False, null=False, verbose_name="Электронная почта"
    )
    comment = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Комментарий"
    )

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
