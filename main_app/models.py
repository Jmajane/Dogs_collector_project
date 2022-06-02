from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Breed(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_breed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Breeder(models.Model):
    name = models.CharField(max_length=150)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="breeds")

    def __str__(self):
        return self.name
    
