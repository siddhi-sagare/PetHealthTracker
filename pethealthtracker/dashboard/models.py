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
    

class Appointment(models.Model):

    APPOINTMENT_TYPE_CHOICES = [
        ("Vet Visit", "Vet Visit"),
        ("Vaccination", "Vaccination"),
        ("Grooming", "Grooming"),
        ("Checkup", "Checkup"),
    ]

    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    appointment_type = models.CharField(
        max_length=50,
        choices=APPOINTMENT_TYPE_CHOICES
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    clinic = models.CharField(
        max_length=100
    )

    notes = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Scheduled"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.pet.name} - {self.appointment_type} ({self.appointment_date})"
    
class Medication(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)   # e.g. 5ml, 1 tablet
    frequency = models.CharField(max_length=50)  # e.g. Twice a day

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication_name} - {self.pet.name}"
    

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email_notifications = models.BooleanField(default=True)
    appointment_reminders = models.BooleanField(default=True)
    medication_reminders = models.BooleanField(default=True)

    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        return f"Settings for {self.user.username}"