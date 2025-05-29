from django.contrib.auth.models import AbstractUser
from django.db import models

from newsletter.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")

    token = models.CharField(max_length=100, verbose_name="token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        permissions = [
            ("set_active", "Может блокировать пользователя ")
        ]

    def __str__(self):
        return self.email

