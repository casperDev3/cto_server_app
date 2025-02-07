from django.db import models

# Create your models here.
class Teammate(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    photo = models.TextField(default="https://loremflickr.com/1280/720")
    age = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    description = models.TextField()