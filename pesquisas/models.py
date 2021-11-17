from django.db import models

#name address country  publication_title publication_number year match type_organization

class Pesquisa(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    publication_title = models.CharField(max_length=400)
    publication_number = models.CharField(max_length=100)
    year = models.IntegerField()
    match = models.CharField(max_length=300)
    type_organization = models.CharField(max_length=50)
    #filtrar_pais = models.CharField(max_length=50)