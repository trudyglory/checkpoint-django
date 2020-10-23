from django.db import models

# Create your models here.
class Voyage(models.Model) : 
    titre = models.CharField(max_length=45)
    datedebut = models
    datefin = 
    
class Ville(models.Voyage): 
    nom = models.CharField(max_length=45)
    
class Date(models):
    date = models.DateTimeField()

class Resume():
    description = models.TextField(max_length=250)

class Ressources():