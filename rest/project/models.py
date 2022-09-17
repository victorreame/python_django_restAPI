from statistics import mode
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)