from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from client.models import Client


class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("client:list")


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
    success_url = reverse_lazy("client:list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("client:list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("client:list")
