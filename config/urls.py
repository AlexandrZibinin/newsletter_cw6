
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("newsletter.urls", namespace="newsletter")),
    path("letter/", include("letter.urls", namespace="letter")),
    path("client/", include("client.urls", namespace="client")),
]
