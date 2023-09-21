from django.db import models

# Create your models here.
class Pessoa(models.Model):
    name = models.CharField(max_length=200)
    idade = models.IntegerField()