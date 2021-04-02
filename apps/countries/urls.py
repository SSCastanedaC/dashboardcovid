from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.countries.views import get_countries, search_countries, get_cases_by_country

urlpatterns = [
    path('countries', login_required(get_countries), name='countries'),
    path('search-countries', login_required(search_countries), name='search-countries'),
    path('cases-country/<str:country_code_alpha_three>', login_required(get_cases_by_country), name='cases-country'),
]