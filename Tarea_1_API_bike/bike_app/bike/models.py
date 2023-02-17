from django.db import models
from django.contrib.postgres.fields import ArrayField


class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

class Extra(models.Model):
    address = models.CharField(max_length=200)
    altitude = models.CharField(max_length=20)
    ebikes = models.BigIntegerField()
    has_bikes = models.BooleanField()
    last_updated = models.BigIntegerField()
    normal_bikes = models.BigIntegerField()
    payment = ArrayField(models.CharField(max_length=20))
    payment_terminal = models.BooleanField()
    renting = models.BigIntegerField()
    returning = models.BigIntegerField() 
    slots = models.BigIntegerField()

class Stations(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    free_bikes = models.BigIntegerField()
    empty_slots = models.BigIntegerField()

class Network(models.Model):
    company = ArrayField(models.CharField(max_length=200))
    gbfs_href = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
