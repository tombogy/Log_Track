
# home/urls.py


# home/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('driver_home/', views.driver_home, name='driver_home'),
    
    
    
]
