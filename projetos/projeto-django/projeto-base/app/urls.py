from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from app.forms.authentication_form import CpfAuthenticationForm
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="login.html",
        authentication_form=CpfAuthenticationForm,
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]