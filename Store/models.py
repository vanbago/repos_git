from email.policy import default
from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="media", blank=True, null=True)
    
    
    def __str__(self) -> str:
        return f"{self.name} en  Stock {self.stock}"
