from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView

app_name = BlogConfig.name

urlpatterns = [
    path("index/", BlogView.as_view(), name="index"),
]