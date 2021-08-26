from django.db import models

class Director(models.Model)
    name = models.CharField(max_length=100,verbose_name="監督")
    def __str__(self):
        return self.name

class Movie(models.Model)
    name = models.CharField(max_length=100,verbose_name="タイトル")
    def __str__(self):
        return self.name

from django.contrib import admin
from yajisanpo.models import StoreType
from yajisanpo.models import Log

admin.site.register(StoreType,Log)
