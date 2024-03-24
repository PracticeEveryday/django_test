from django.contrib import admin
from django.urls import path, include

from app import views as app_views

urlpatterns = [
    path("boards/", include("app.urls")),
    path("users/", include("user.urls")),

    path("app/", app_views.index),
    # 정수 인자가 오면 pk라는 이름으로 post_detail 함수 호출 시 인자로 넘겨주겠다!
    path("app/<int:pk>/", app_views.post_detail),

    path('admin/', admin.site.urls),
]
