from django.db import models
from django.conf import settings

class User(models.Model):
    cpf = models.CharField(max_length=11, unique=True, error_messages={
        'unique': 'Já existe um usuario com esse CPF cadastrado.'
    })
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_record',
    )