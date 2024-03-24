from django.contrib import admin
from django.urls import path, include

from app import views as app_views

urlpatterns = [
    path("boards/", include("app.urls")),
    path("users/", include("user.urls")),
    path("app/", app_views.index),
    path('admin/', admin.site.urls),
]
