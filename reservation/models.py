from django.db import models

# Create your models here.
class Reservation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    book_name =  models.CharField(max_length=30 ,default="blank")
    reserved_to =  models.CharField(max_length=30)