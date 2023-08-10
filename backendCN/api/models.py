from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=100, null=True,blank=True)
    email = models.CharField(max_length=100, null=True,blank=True)
    phone = models.CharField(max_length=100, null=True,blank=True)
    Birth_date = models.DateField(null=True,blank=True)