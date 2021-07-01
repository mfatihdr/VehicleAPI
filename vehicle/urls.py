from django.urls import include, path
from .views import VehicleCreate, VehicleUpdate, VehicleDelete, VehicleGet, VehicleModelCreate
urlpatterns = [
    path('create/', VehicleCreate.as_view(), name='create-vehicle'),
    path('create_model/', VehicleModelCreate.as_view(), name='create-vehicle-model'),
    path('<int:veh_id>/', VehicleGet.as_view(), name='list-vehicle'),
    path('<int:veh_id>/update/', VehicleUpdate.as_view(), name='update-vehicle'),
    path('<int:veh_id>/delete/', VehicleDelete.as_view(), name='delete-vehicle'),
]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     