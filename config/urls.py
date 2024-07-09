from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("newsletter.urls", namespace="newsletter")),
    path("", include("letter.urls", namespace="letter")),
    path("", include("client.urls", namespace="client")),
    path("users/", include("users.urls", namespace="users")),
]
