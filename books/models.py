from django.db import models

# Create your models here.

class Books(models.Model):
	name = models.CharField(max_length=30)
	price = models.CharField(max_length=30)
	is_available = models.BooleanField(default= True) 
	is_reserved = models.BooleanField(default= False) 
	alloted_to =  models.CharField(max_length=30)