from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
)
from pytils.translit import slugify

from blog.models import Blog


class BlogView(TemplateView):
    model = Blog

    template_name = "blog/index.html"