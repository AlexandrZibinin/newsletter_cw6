from client.apps import ClientConfig
from django.urls import path

from client.views import (
    ClientCreateView,
    ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView,
)

app_name = ClientConfig.name

urlpatterns = [
    path("client/list/", ClientListView.as_view(), name="list"),
    path("client/create/", ClientCreateView.as_view(), name="create"),
    path("client/list/<int:pk>/", ClientDetailView.as_view(), name="detail"),
    path("client/list/<int:pk>/", ClientUpdateView.as_view(), name="update"),
    path("client/list/<int:pk>/", ClientDeleteView.as_view(), name="delete"),
]
