
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from letter.models import Letter


class LetterCreateView(CreateView):
    model = Letter
    fields = "__all__"
    success_url = reverse_lazy("letter:list")


class LetterListView(ListView):
    model = Letter


class LetterDetailView(DetailView):
    model = Letter
    success_url = reverse_lazy("letter:list")


class LetterUpdateView(UpdateView):
    model = Letter
    fields = "__all__"
    success_url = reverse_lazy("letter:list")


class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy("letter:list")
