from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView,
)
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

