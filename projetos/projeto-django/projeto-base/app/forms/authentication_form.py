from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CpfAuthenticationForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(strip=False)