from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=2000)
    project_url = models.URLField(max_length=200)
    document_type = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    typology = models.CharField(max_length=20)
    owner = models.CharField(max_length=200)
    investment = models.DecimalField(max_digits=5, decimal_places=4)
    presentation_date = models.DateField()
    status = models.CharField(max_length=200)
    map = models.URLField(max_length=200)
