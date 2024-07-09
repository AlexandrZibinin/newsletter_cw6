from django.db import models

from newsletter.models import NULLABLE


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
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="Владелец", **NULLABLE)


    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
