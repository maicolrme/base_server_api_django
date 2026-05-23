from django.urls import path
from .views import SendNotificationView, TestNotificationView, RegisterTokenView

urlpatterns = [
    path("send", SendNotificationView.as_view()),
    path("test", TestNotificationView.as_view()),
    path("register-token", RegisterTokenView.as_view()),
]
