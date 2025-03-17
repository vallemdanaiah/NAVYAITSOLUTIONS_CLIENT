from django.db import models

# Create your models here.
class GetinTouch(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)  
    subject = models.CharField(max_length=255)  
    message = models.TextField()  



class OnlineTraining(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=255)  
    phone = models.CharField(max_length=15, blank=True, null=True)  
    collage = models.CharField(max_length=255) 
    branch = models.CharField(max_length=100)  
    year = models.CharField(max_length=10)  


class ApplyForProject(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=255)  
    phone = models.CharField(max_length=15, blank=True, null=True)  
    collage= models.CharField(max_length=255)  
    branch = models.CharField(max_length=100)  
    year = models.CharField(max_length=10)  