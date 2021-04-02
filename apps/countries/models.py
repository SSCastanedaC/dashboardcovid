from django.db import models

# Create your models here.

class Country(models.Model):
    name_spanish = models.CharField(max_length=100)
    name_english = models.CharField(max_length=100)
    slug_spanish = models.SlugField(max_length=100)
    slug_english = models.SlugField(max_length=100)
    code_alpha_two = models.CharField(max_length=5)
    code_alpha_three = models.CharField(max_length=5)