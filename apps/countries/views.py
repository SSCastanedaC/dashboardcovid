from django.shortcuts import render, get_object_or_404
from apps.countries.models import Country
from django.template.defaultfilters import slugify
from dashboardcovid.settings import headers_rapidapi
import requests
import json
from googletrans import Translator
import datetime
import time

# Create your views here.

def save_countries():
    Country.objects.all().delete()
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.request('GET', url)
    countries = response.json()
    available_countries = []
    for country in countries:
        country_name_en = country['name']
        try:
            translator = Translator()
            translation = translator.translate(country_name_en, dest='spanish')
            country_name_es = str(translation.text)
        except:
            country_name_es = country_name_en
        new_country = Country()
        new_country.name_spanish = country_name_es
        new_country.name_english = country_name_en
        new_country.slug_spanish = slugify(country_name_en)
        new_country.slug_english = slugify(country_name_en)
        new_country.code_alpha_two = country['alpha2Code']
        new_country.code_alpha_three = country['alpha3Code']
        available_countries.append(new_country)
    Country.objects.bulk_create(available_countries)
    context = {}
    return True

def get_countries(request):
    countries = Country.objects.all()
    context = {
        'countries': countries
    }
    return render (request, 'web/countries.html', context)

def get_cases_by_country(request, country_code_alpha_three):
    country = get_object_or_404(Country, code_alpha_three = country_code_alpha_three)
    #General
    url = 'https://covid-19-data.p.rapidapi.com/country/code'
    querystring = {
        'code': country.code_alpha_three,
    }
    response = requests.request('GET', url, headers=headers_rapidapi, params=querystring)
    cases = response.json()
    time.sleep(1)
    #Provincias
    url = 'https://covid-19-data.p.rapidapi.com/report/country/code'
    querystring = {
        'code': country.code_alpha_three,
        'date': '2020-06-18'
    }
    response = requests.request('GET', url, headers=headers_rapidapi, params=querystring)
    provinces = response.json()
    context = {
        'country': country,
        'cases': cases,
        'provinces': provinces
    }
    return render (request, 'web/cases_by_country.html', context)
    