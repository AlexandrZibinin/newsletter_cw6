from django.db import models


class Letter(models.Model):
    title = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Тема"
    )
    text = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Тело"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"