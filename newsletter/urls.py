from newsletter.apps import NewsletterConfig
from django.urls import path

app_name = NewsletterConfig.name

urlpatterns = [
    # path("create/", NewsletterCreateView.as_view(), name="create newsletter"),
]