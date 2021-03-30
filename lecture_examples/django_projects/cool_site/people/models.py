from django.db import models
from django.db.models.deletion import SET_NULL

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=6)

class Person(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email = models.EmailField()
    # profile_pic =  models.ImageField(blank=True)
    profile_pic =  models.ImageField(upload_to="images/")
    address = models.ForeignKey(Address, on_delete=SET_NULL, null=True)
    