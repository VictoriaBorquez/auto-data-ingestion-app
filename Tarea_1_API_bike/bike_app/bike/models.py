from django.db import models
from django.contrib.postgres.fields import ArrayField

class Extra(models.Model):
    address = models.CharField(max_length=200)
    altitude = models.CharField(max_length=20)
    ebikes = models.BigIntegerField()
    has_bikes = models.BooleanField()
    last_updated = models.BigIntegerField()
    normal_bikes = models.BigIntegerField()
    payment = ArrayField(models.CharField(max_length=20))
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=20)
    renting = models.BigIntegerField()
    returning = models.BigIntegerField() 
    slots = models.BigIntegerField()
    uid = models.CharField(max_length=20)

class Stations(models.Model):
    id_station = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    free_bikes = models.BigIntegerField()
    empty_slots = models.BigIntegerField()
    extra = models.OneToOneField(Extra, on_delete=models.CASCADE, primary_key = True)

class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

class Network(models.Model):
    company = ArrayField(models.CharField(max_length=200))
    gbfs_href = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    id_network = models.CharField(max_length=200)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    stations = models.ForeignKey(Stations, on_delete= models.CASCADE)