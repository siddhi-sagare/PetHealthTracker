from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20)   # Dog / Cat
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)     # Male / Female
    weight = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
