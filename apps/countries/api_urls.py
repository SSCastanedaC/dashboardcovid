from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.countries.api import get_countries

urlpatterns = [
    path('countries', login_required(get_countries), name='countries')
]