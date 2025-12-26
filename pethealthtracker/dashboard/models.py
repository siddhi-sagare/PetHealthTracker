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


class HealthRecord(models.Model):

    EVENT_CHOICES = [
        ("Vaccination", "Vaccination"),
        ("Vet Visit", "Vet Visit"),
        ("Injury", "Injury"),
        ("Checkup", "Checkup"),
        ("Other", "Other"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="health_records"
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="health_records"
    )

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_CHOICES
    )

    event_date = models.DateField()

    description = models.TextField()

    veterinarian = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.pet.name} - {self.event_type}"