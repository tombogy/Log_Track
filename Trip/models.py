from django.db import models
from Driver.models import Driver
from Category.models import Category
from datetime import date
# Create your models here.
class Trip(models.Model):
    trip_from = models.CharField(max_length=500, verbose_name='Source')
    trip_to = models.CharField(max_length=500, verbose_name='Destination')
    credit_point = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time=  models.TimeField(null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    
class TripDetails ( models.Model):
    
    
    
    
    
    
    
    
    
    
    
    
    
    Trip From (Source)
Trip To (Destination)
Credit Point
Category Name
Trip Taken Date:
Report Date for Taken:
Report Time: