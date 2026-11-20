from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.db import transaction
from django.contrib.auth.models import Group

from app.forms.change_password_form import ChangePasswordForm
from app.forms.create_user_form import CreateUserForm
from app.decorators import group_required
from .groups import USER_GROUP, ADMIN_GROUP

from uuid import uuid4

@group_required(ADMIN_GROUP)
def create_user(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        
        if user_form.is_valid():
            User = get_user_model()

            with transaction.atomic():
                user = user_form.save(commit=False)
                user.ticket_number = str(uuid4())
                user.save()

                user = User.objects.create_user(
                    username=user.cpf,
                    password=user_form.cleaned_data['password'],
                )
                user.user = user
                user.save(update_fields=['user'])
                user.groups.add(Group.objects.get(name=USER_GROUP))
                
            return redirect('users')
    else:
        user_form = CreateUserForm()
        
    response = { 
        'form': user_form 
    }
        
    return render(request, 'create-user.html', response)

@group_required(USER_GROUP)
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, user=request.user)

        if form.is_valid():
            request.user.set_password(form.cleaned_data["new_password"])
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect("my_user")
    else:
        form = ChangePasswordForm(user=request.user)

    return render(request, "change-password.html", {"form": form})