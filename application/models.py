# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Fournisseur(models.Model):
    nom=models.CharField(max_length=50)
    adresse= models.CharField(max_length=50)
    email=models.CharField(max_length=100)


class Article(models.Model):
    nom=models.CharField(max_length=50)
    modele= models.CharField(max_length=50)
    couleur=models.CharField(max_length=20)
    prix_achat= models.FloatField()
    prix_vente= models.FloatField()
    stockage= models.FloatField()
    ram= models.FloatField()
    apn= models.CharField(max_length=20)
    taille=models.CharField(max_length=20)
    version=models.CharField(max_length= 20)
    fournisseur=models.ForeignKey(Fournisseur, on_delete=models.CASCADE)



class Client(models.Model):
    photo=models.URLField()
    adresse= models.CharField(max_length=50)
    user= models.OneToOneField(User, on_delete=models.CASCADE)

class Commande(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    article=models.OneToOneField(Article,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)

class Livraison(models.Model):
    date= models.DateField(default=timezone.now)
    commande=models.OneToOneField(Commande,on_delete=models.CASCADE)


    

