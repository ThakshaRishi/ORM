from django.db import models
from django.contrib import admin
class Football (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    team=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    height=models.IntegerField()
class FootballAdmin(admin.ModelAdmin):
    list_display=('name','age','team','position','height')

# Create your models here.
