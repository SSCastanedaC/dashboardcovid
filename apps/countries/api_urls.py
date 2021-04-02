from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.countries.api import get_countries

urlpatterns = [
    path('countries', get_countries, name='countries')
]