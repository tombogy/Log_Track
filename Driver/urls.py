from django.urls import path
from . import views


urlpatterns = [
    path('driver_home01',views.homepage_driver, name='driver_home01'),
    path('driver_add',views.add_driver, name='driver_add'),
    path('driver_update/<int:did>/', views.update_driver, name='update_driver'),
    path('driver_delete/<int:did>/', views.delete_driver, name='delete_driver'),
]