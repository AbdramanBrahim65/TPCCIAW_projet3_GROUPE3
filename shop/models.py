from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Category(models.Model):
    choice = (
        ("Téléphone","Téléphone"),
        ("Télévision","Télévision"),
        ("Ordinateur","Ordinateur")
    )
    name = models.CharField(max_length=200,choices = choice)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name    


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='image_publie', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']  

    def __str__(self):
        return self.title           

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200,null=True)
    ville = models.CharField(max_length=20,null=True)
    pays = models.CharField(max_length=300,null=True)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom   

   