from django.shortcuts import render
from apps.cases.models import Case
from dashboardcovid.settings import headers_rapidapi
import requests
import datetime
import json

# Create your views here.

def get_home(request):
    url = 'https://covid-19-data.p.rapidapi.com/report/totals'
    response = requests.request('GET', url, headers=headers_rapidapi)
    cases = response.json()
    context = {
        'cases': cases,
    }
    return render (request, 'web/home.html' ,context)