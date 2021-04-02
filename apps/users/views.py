from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.users.forms import CreateUserForm
from django.contrib.auth import password_validation

# Create your views here.

def create_user(request):
    context = {}
    if request.method == 'POST':
        form_user = CreateUserForm(request.POST)
        if form_user.is_valid():
            try:
                password = form_user.data['password']
                print(password)
                form_user = form_user.save(commit = False)
                password_validation.validate_password(password)
                form_user.set_password(password)
                form_user.save()
                return redirect ('login')
            except Exception as e:
                context['errors_1'] = e
        else:
            context['errors_2'] = form_user.errors
    return render(request, 'web/create_user.html', context)