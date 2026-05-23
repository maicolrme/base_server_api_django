from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("app.authentication.urls")),
    path("items/", include("app.items.urls")),
    path("users/", include("app.users.urls")),
    path("notifications/", include("app.notifications.urls")),
    path("doc/", SpectacularAPIView.as_view(), name="schema"),
    path("ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("", SpectacularRedocView.as_view(url_name="schema"), name="home"),
]
