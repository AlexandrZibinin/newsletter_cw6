from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter, Mailing


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("newsletter:list")
    
    def form_valid(self, form):
        news = form.save()
        user = self.request.user
        news.owner = user
        news.save()
        
        return super().form_valid(form)


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter


class NewsletterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy("newsletter:list")
    permission_required = 'newsletter.set_'
    
    


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy("newsletter:list")


def index(request):
    return render(request, "base.html")


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
