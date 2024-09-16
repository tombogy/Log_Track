from django.urls import path
from . import views


urlpatterns = [
    path('vehicle_home01/', views.homepage_vehicle, name='vehicle_home01'),
    path('vehicle_add',views.add_vehicle, name='vehicle_add'),
    path('vehicles/update/<int:vehicle_id>/', views.update_vehicle, name='update_vehicle'), 
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
]