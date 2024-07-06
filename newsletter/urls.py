from newsletter.apps import NewsletterConfig
from django.urls import path

from newsletter.views import (
    NewsletterCreateView,
    NewsletterDetailView,
    NewsletterUpdateView,
    NewsletterDeleteView,
    ClientCreateView, index, NewsletterListView, ClientListView,
)

app_name = NewsletterConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("newsletter/list", NewsletterListView.as_view(), name="list newsletter"),
    path("newsletter/create", NewsletterCreateView.as_view(), name="create newsletter"),
    path("newsletter/list/<int:pk>/", NewsletterDetailView.as_view(), name="detail newsletter"),
    path("newsletter/list/<int:pk>/", NewsletterUpdateView.as_view(), name="update newsletter"),
    path("newsletter/list/<int:pk>/", NewsletterDeleteView.as_view(), name="delete newsletter"),

    path("clients/list", ClientListView.as_view(), name="list clients"),
    path("clients/create", ClientCreateView.as_view(), name="create clients"),
    path("clients/list/<int:pk>/", ClientCreateView.as_view(), name="detail clients"),
    path("clients/list/<int:pk>/", ClientCreateView.as_view(), name="update clients"),
    path("clients/list/<int:pk>/", ClientCreateView.as_view(), name="delete clients"),

]
