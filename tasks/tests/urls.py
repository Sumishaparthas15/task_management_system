from django.urls import path, include
from tasks.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]
