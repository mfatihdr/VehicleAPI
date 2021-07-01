from django.db import models
from django.conf import settings
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User

class base_vehicle(models.Model):
    created_on = models.DateTimeField(auto_now = True)
    modified_on = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
       abstract = True

class VehicleModel(models.Model):
    model = models.CharField( max_length=240)
    brand = models.CharField( max_length=240)
    
    def __str__(self):
        return '{}: {}'.format(self.brand, self.model)

class Vehicle(base_vehicle):
    veh_id = models.AutoField(primary_key=True)
    WHITE = 'white'
    GREEN = 'green'
    YELLOw = 'yellow'
    BLACK = 'black'
    COLOR_CHOICES = (
        ('WHITE', 'white'),
        ('GREEN', 'green'),
        ('YELLOW', 'yellow'),
        ('BLACK', 'black'),
    )
    km = models.PositiveIntegerField(help_text='Enter field documentation')
    plaka = models.CharField(max_length=240, help_text='Enter field documentation')
    sase_numarasi = models.IntegerField(help_text='Enter field documentation')
    renk = models.CharField(max_length=6, choices=COLOR_CHOICES, default='WHITE')
    vehicle_model = models.ManyToManyField(VehicleModel)

    def __str__(self):
        return self.veh_id


