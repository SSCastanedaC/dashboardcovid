from django.shortcuts import render
from apps.cases.models import Case

# Create your views here.

def get_home(request):
    context = {}
    return render(request, 'web/home.html' ,context)