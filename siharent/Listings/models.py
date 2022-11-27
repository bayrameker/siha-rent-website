from datetime import datetime
from email.policy import default
from django.db import models
from Sihas.models import Sihas
# Create your models here.


class Listings(models.Model):
    sihas = models.ForeignKey(Sihas, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    altitude = models.IntegerField()
    flight_time = models.IntegerField()
    took_off = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    country = models.CharField(max_length=20)
    gps_independence = models.BooleanField(default=True)
    auto_antenna = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

