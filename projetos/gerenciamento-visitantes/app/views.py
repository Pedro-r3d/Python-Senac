from django.shortcuts import render, redirect
from datetime import datetime
from uuid import uuid4

from .models import Visitor

# Create your views here.
def home(request):
    return render(request, 'home.html')

def visitors(request):
    visitors = Visitor.objects.all()

    response = {
        'visitors': visitors
    }

    return render(request, 'visitors.html', response)

def create_visitor(request):
    if request.method == 'POST':
        visitor = Visitor()

        visitor.first_name = request.POST['first_name']
        visitor.last_name = request.POST['last_name']
        visitor.cpf = request.POST['cpf']
        visitor.birth_date = datetime.strptime(request.POST['birth_date'], '%Y-%m-%d')
        visitor.ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d')
        visitor.ticket_type = request.POST['ticket_type']
        visitor.ticket_number = str(uuid4())

        visitor.save()

        return redirect('visitors')

    return render(request, 'create-visitor.html')

def update_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)
    if request.method == 'POST':
        visitor.first_name = request.POST['first_name']
        visitor.last_name = request.POST['last_name']
        visitor.cpf = request.POST['cpf']
        visitor.birth_date = datetime.strptime(request.POST['birth_date'], '%Y-%m-%d')
        visitor.ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d')
        visitor.ticket_type = request.POST['ticket_type']

        visitor.save()

        return redirect('visitors')

    response = {
        'visitor': visitor    
    }

    return render(request, 'update-visitor.html', response)

def delete_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)

    visitor.delete()

    return redirect('visitors')