from datetime import datetime
from email.policy import default
from django.db import models
# Create your models here.

class Sihas(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weight = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name