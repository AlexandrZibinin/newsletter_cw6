from newsletter.apps import NewsletterConfig
from django.urls import path

from newsletter.views import (
    NewsletterCreateView,
    NewsletterDetailView,
    NewsletterUpdateView,
    NewsletterDeleteView,
    NewsletterListView,
    index,
)

app_name = NewsletterConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("newsletter/list/", NewsletterListView.as_view(), name="list"),
    path("newsletter/create", NewsletterCreateView.as_view(), name="create"),
    path("newsletter/list/<int:pk>/", NewsletterDetailView.as_view(), name="detail"),
    path("newsletter/<int:pk>/update", NewsletterUpdateView.as_view(), name="update"),
    path("newsletter/<int:pk>/delete", NewsletterDeleteView.as_view(), name="delete"),
]
