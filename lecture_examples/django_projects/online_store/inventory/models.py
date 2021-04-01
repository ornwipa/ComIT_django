from django.db import models

class Review(models.Model):
    score = models.IntegerField()
    comment = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    reviews = models.ManyToManyField(Review)
