from django.db import models

# Create your models here.
class vehicle(models.Model):
    v_name = models.CharField(max_length=100)
    v_number= models.CharField(max_length=15)
    c_number = models.EmailField(max_length=100)
    v_photo = models.ImageField(upload_to='driver_photos/')

    def __str__(self):
        return self.v_name