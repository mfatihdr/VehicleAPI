from rest_framework import serializers
from .models import Vehicle, VehicleModel
from django import forms

class VehicleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle 
        fields = ['veh_id', 'km', 'plaka', 'sase_numarasi', 'renk', 'vehicle_model']
        widgets = {'created_on': forms.HiddenInput(),
                   'modified_on': forms.HiddenInput(),
                   'is_active': forms.HiddenInput(),
                   'is_deleted': forms.HiddenInput(),
                   'deleted_at': forms.HiddenInput()
                    }

class VehicleDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle 
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleModel 
        fields = ['model', 'brand']
