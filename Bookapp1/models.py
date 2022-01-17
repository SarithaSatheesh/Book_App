from django.db import models

# Create your models here.
class BookappModel(models.Model):
    Bname=models.CharField(max_length=50)
    Bid=models.IntegerField()
    Author=models.CharField(max_length=50)
    Read_by=models.CharField(max_length=50)

