from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from newsletter.models import Newsletter, Client


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = "__all__"
    success_url = reverse_lazy("newsletters:list")


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = "__all__"
    success_url = reverse_lazy("newsletters:list")


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy("newsletters:list")


class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("clients:list")


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
    success_url = reverse_lazy("clients:list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("clients:list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("clients:list")


def index(request):

    return render(request, 'base.html')