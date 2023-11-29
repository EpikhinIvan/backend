from django.db import models

class Eat(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    count = models.IntegerField()