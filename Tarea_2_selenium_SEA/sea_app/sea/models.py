from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=2000)
    document_type = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    typology = models.CharField(max_length=20)
    owner = models.CharField(max_length=200)
    investment = models.CharField(max_length=2000)
    presentation_date = models.DateField()
    status = models.CharField(max_length=200)
