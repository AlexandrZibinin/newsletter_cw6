from letter.apps import LetterConfig
from django.urls import path

from letter.views import (
    LetterCreateView, LetterListView, LetterUpdateView, LetterDetailView, LetterDeleteView,
)

app_name = LetterConfig.name

urlpatterns = [
    path("letter/list/", LetterListView.as_view(), name="list"),
    path("letter/create/", LetterCreateView.as_view(), name="create"),
    path("letter/list/<int:pk>/", LetterDetailView.as_view(), name="detail"),
    path("letter/list/<int:pk>/", LetterUpdateView.as_view(), name="update"),
    path("letter/list/<int:pk>/", LetterDeleteView.as_view(), name="delete"),
]
