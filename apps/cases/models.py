from django.db import models
from apps.countries.models import Country

# Create your models here.

class Case(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    date = models.DateField()
    active = models.IntegerField()
    confirmed = models.IntegerField()
    critical = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()