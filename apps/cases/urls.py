from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.cases.views import get_home

urlpatterns = [
    path('home', login_required(get_home), name='home')
]