from django.shortcuts import render
from .models import Vehicle, VehicleModel
from rest_framework import generics,mixins
from .serializers import VehicleCreateSerializer,VehicleModelSerializer,VehicleDeleteSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

class VehicleCreate(generics.CreateAPIView):
    queryset = Vehicle.objects.all(),
    serializer_class = VehicleCreateSerializer

class VehicleUpdate(generics.UpdateAPIView):
    serializer_class = VehicleCreateSerializer
    lookup_field = 'veh_id'
    def get_object(self, queryset=None):
        return get_object_or_404(Vehicle, veh_id=self.kwargs["veh_id"])
    
    def form_valid(self, form):
        return super().form_valid(form)

class VehicleGet(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = VehicleCreateSerializer  
    
    def get_object(self, queryset=None):
        return get_object_or_404(Vehicle, veh_id=self.kwargs["veh_id"])

    @method_decorator(cache_page(5), name='dispatch')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
            
class VehicleDelete(generics.RetrieveDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDeleteSerializer
    lookup_field = 'veh_id'

class VehicleModelCreate(generics.CreateAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
