from tabnanny import verbose
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    author = models.CharField(max_length=128)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    category = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f"{self.author, self.title}"
    
class Categorie(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to ="photo/", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    

