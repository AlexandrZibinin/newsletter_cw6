from django.views.decorators.cache import cache_page

from newsletter.apps import NewsletterConfig
from django.urls import path

from newsletter.views import (
    NewsletterCreateView,
    NewsletterDetailView,
    NewsletterUpdateView,
    NewsletterDeleteView,
    NewsletterListView,
    index, MailingListView,
)

app_name = NewsletterConfig.name

urlpatterns = [
    path("", cache_page(60)(index), name="index"),
    path("newsletter/list/", cache_page(60)(NewsletterListView.as_view()), name="list"),
    path("newsletter/create", NewsletterCreateView.as_view(), name="create"),
    path("newsletter/list/<int:pk>/", NewsletterDetailView.as_view(), name="detail"),
    path("newsletter/<int:pk>/update", NewsletterUpdateView.as_view(), name="update"),
    path("newsletter/<int:pk>/delete", NewsletterDeleteView.as_view(), name="delete"),
    path("mailing/list/", MailingListView.as_view(), name="list_mailing"),
]
