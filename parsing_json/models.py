from django.db import models


# Create your models here.

class DataRowModel(models.Model):
    region = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    value = models.FloatField(null=True, blank=True)
