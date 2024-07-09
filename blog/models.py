from django.db import models

from newsletter.models import NULLABLE


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(max_length=1000, verbose_name="Статья")
    image = models.ImageField(upload_to="blog/images", verbose_name="Kартинка", **NULLABLE)
    count_views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return f"{self.title}"
