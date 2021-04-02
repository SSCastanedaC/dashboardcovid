from django.urls import include, path
from apps.users.views import create_user

urlpatterns = [
    path('create-user', create_user, name='create-user'),
]