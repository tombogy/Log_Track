from django.urls import path
from . import views


urlpatterns = [
    path('category_home01',views.category_home, name='category_home01'),
    path('category_add',views.add_category, name='category_add'),
    path('category_update/<int:category_id>/', views.update_category, name='category_update'), 
    path('category_delete/<int:category_id>/', views.delete_category, name='category_delete'),
]