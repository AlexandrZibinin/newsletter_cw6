from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from letter.forms import LetterForm
from letter.models import Letter


class LetterCreateView(CreateView, LoginRequiredMixin):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy("letter:list")

    def form_valid(self, form):
        letter = form.save()
        user = self.request.user
        letter.owner = user
        letter.save()

        return super().form_valid(form)


class LetterListView(LoginRequiredMixin, ListView):
    model = Letter


class LetterDetailView(LoginRequiredMixin, DetailView):
    model = Letter
    success_url = reverse_lazy("letter:list")


class LetterUpdateView(LoginRequiredMixin, UpdateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy("letter:list")


class LetterDeleteView(LoginRequiredMixin, DeleteView):
    model = Letter
    success_url = reverse_lazy("letter:list")
