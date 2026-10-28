from django.shortcuts import render, redirect
from django.db.models import Count
from datetime import datetime
from uuid import uuid4
from django.db.models import Q
from datetime import date
from django.db.models import Avg
from django.db.models.functions import ExtractYear, Now


from django.db.models import Q

from .models import Visitor

# Create your views here.
def home(request):
    return render(request, 'home.html')

def visitors(request):
    search = request.GET.get('name_or_cpf', '').strip()
    ticket_type = request.GET.get('ticket_type', '')
    search_date = request.GET.get('ticket_date', '')
    order_by_id = request.GET.get('order_by_id','1')

    visitors = Visitor.objects.annotate(
        calculated_age=ExtractYear(Now()) - ExtractYear('birth_date'))
            
    visitors = visitors.filter(
        Q(first_name__icontains=search)
        | Q(last_name__icontains=search)
        | Q(cpf__icontains=search),
        )
    


    if order_by_id == '1':
        visitors = visitors.order_by('first_name')
    elif order_by_id == '2':
        visitors = visitors.order_by('first_name').reverse()

    if order_by_id == '3':
        visitors = visitors.order_by('calculated_age').reverse()
    elif order_by_id == '4':
        visitors = visitors.order_by('calculated_age')

    if ticket_type:
        visitors = visitors.filter(ticket_type=ticket_type)


    print(search_date)
    if search_date:
        visitors = visitors.filter(ticket_date=search_date)

    response = {
        'visitors': visitors,
        'search' : search,
        'ticket_type' : ticket_type,
        'ticket_date' : search_date,
        'order_by_id': order_by_id
      
    } 
    print(response)
    return render(request, 'visitors.html', response)

def create_visitor(request):
    if request.method == 'POST':
        visitor = Visitor()

        visitor.first_name = request.POST['first_name']
        visitor.last_name = request.POST['last_name']
        
        visitor.cpf = request.POST['cpf']
        if Visitor.objects.filter(cpf=visitor.cpf).exists():
            return render(request, 'create-visitor.html',{
                'erroCpf': 'Visitante com CPF já registrado'
            })
    
        visitor.birth_date = datetime.strptime(request.POST['birth_date'], '%Y-%m-%d')
        visitor.ticket_date = date.strptime(request.POST['ticket_date'], '%Y-%m-%d')
        if visitor.ticket_date < date.today():
            return render(request, 'create-visitor.html', {
                'erroDate': 'Data não pode ser inferior a de hoje.'
            })
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


def statics(request):
    visitor_total = Visitor.objects.count()
    visitor_normal = Visitor.objects.filter(ticket_type=1).count()
    visitor_vip = Visitor.objects.filter(ticket_type=2).count()
    visitor_premium = Visitor.objects.filter(ticket_type=3).count()

    result = Visitor.objects.annotate(
        age=ExtractYear(Now()) - ExtractYear('birth_date')
    ).aggregate(
        media_age=Avg('age')
    )
    visitor_media = result['media_age']

    response = {
        'visitor_total' : visitor_total,
        'visitor_normal' : visitor_normal,
        'visitor_vip' : visitor_vip,
        'visitor_premium' : visitor_premium,
        'visitor_age' : visitor_media
    }
    return render(request, 'statics.html', response)

def grafic_pizza_view(request):
    
    dados = (
        Visitor.object.values('ticket_type').annotate(total=Count('id')).order_by('-total')
    )
    labels = [item['ticket_type'] for item in dados]
    values = [item['total'] for item in dados]

    response = {
        'labels' : labels,
        'values' : values
    }
    return(request, 'statics.html', response)