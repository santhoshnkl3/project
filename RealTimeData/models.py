from django.db import models

# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=32)
    email= models.EmailField()

class LiveLocaiton(models.Model):
    lattitude = models.CharField(max_length=32)
    longitude = models.CharField(max_length=32)

    def __str__(self):
        return "Lattitude : "+self.lattitude+" Longitude : "+self.longitude