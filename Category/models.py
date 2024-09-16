from django.db import models

# Create your models here.
class Category(models.Model):
    #did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tot_bag= models.CharField(max_length=15)
    bag_wei = models.EmailField(max_length=100)
    tot_wei= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    