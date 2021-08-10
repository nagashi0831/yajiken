from django.db import models

class StoreType(models.Model)
    name = models.CharField(max_length=100,verbose_name="お店の種類")
    def __str__(self):
        return self.name

class Log(models.Model)
    name = models.CharField(max_length=100,verbose_name="履歴")
    def __str__(self):
        return self.name

from django.contrib import admin
from yajisanpo.models import StoreType
from yajisanpo.models import Log

admin.site.register(StoreType,Log)
