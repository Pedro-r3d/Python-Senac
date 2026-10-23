from django.shortcuts import render, redirect
from datetime import datetime
from uuid import uuid4
<<<<<<< HEAD
=======
from django.db.models import Q
>>>>>>> 68a88759a20ac4732014fefcfd531ad508b3f4a5

from .models import Visitor

# Create your views here.
def home(request):
    return render(request, 'home.html')

def visitors(request):
    search = request.GET.get('name_or_cpf', '').strip()
    ticket_type = request.GET.get('ticket_type', '')

    visitors = Visitor.objects.all()

    visitors = visitors.filter(
        Q(first_name__icontains=search)
        | Q(last_name__icontains=search)
        | Q(cpf__contains=search),
        Q(ticket_type__contains=ticket_type)
        )

    response = {
        'visitors': visitors,
        'search' : search,
        'ticket_type' : ticket_type
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