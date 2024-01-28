from django.db import models

from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField()
    available_for_adoption = models.BooleanField(default=True)
    adopter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'name: {self.name}, species: {self.species}'
    
class AdoptionApplication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adopter = models.ForeignKey(User, on_delete=models.CASCADE)
    application_text = models.TextField()
    is_approved = models.BooleanField(default=False)

