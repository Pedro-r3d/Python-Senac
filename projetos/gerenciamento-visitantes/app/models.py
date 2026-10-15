from django.db import models

# Create your models here.
class Visitor(models.Model):
    class TicketType(models.IntegerChoices):
        NORMAL = 1, 'Normal'
        VIP = 2, 'VIP'
        PREMIUM = 3, 'Premium'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    ticket_date = models.DateField()
    ticket_type = models.IntegerField(choices=TicketType.choices)
    ticket_number = models.CharField(255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
