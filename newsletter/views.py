from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from newsletter.models import Newsletter, Mailing


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = (
        "first_send",
        "period",
        "client",
        "message",
    )
    success_url = reverse_lazy("newsletter:list")


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = (
        "first_send",
        "period",
        "status",
        "client",
        "message",
    )
    success_url = reverse_lazy("newsletter:list")


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy("newsletter:list")


def index(request):
    return render(request, "base.html")


class MailingListView(ListView):
    model = Mailing
