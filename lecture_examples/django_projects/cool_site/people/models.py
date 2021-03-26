from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email = models.EmailField()
    # profile_pic =  models.ImageField(blank=True)
    profile_pic =  models.ImageField(upload_to="images/")
    