from django.db import models
from django.contrib.auth.models import User
# Imports Django ORM tools and built-in User model for authentication

# pet page:
class Pet(models.Model):
    # Links each pet to a specific logged-in user
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Basic pet information
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20)   # Dog / Cat
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()           # Age in years
    gender = models.CharField(max_length=10)     # Male / Female
    weight = models.FloatField()                  # Weight of pet
    
    # Automatically stores record creation date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Human-readable representation in admin & shell
        return self.name


# healthrecord page:
class HealthRecord(models.Model):
    # Predefined event types for consistency
    EVENT_CHOICES = [
        ("Vaccination", "Vaccination"),
        ("Vet Visit", "Vet Visit"),
        ("Injury", "Injury"),
        ("Checkup", "Checkup"),
        ("Other", "Other"),
    ]

    # Owner of the health record
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="health_records"
    )

    # Pet associated with this health record
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="health_records"
    )

    # Type of health event
    event_type = models.CharField(
        max_length=50,
        choices=EVENT_CHOICES
    )

    # Date when the event occurred
    event_date = models.DateField()

    # Detailed description of the event
    description = models.TextField()

    # Veterinarian or clinic name
    veterinarian = models.CharField(
        max_length=100
    )

    # Automatically records creation timestamp
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        # Displays pet name and event type
        return f"{self.pet.name} - {self.event_type}"


# appointment page:
class Appointment(models.Model):
    # Appointment categories
    APPOINTMENT_TYPE_CHOICES = [
        ("Vet Visit", "Vet Visit"),
        ("Vaccination", "Vaccination"),
        ("Grooming", "Grooming"),
        ("Checkup", "Checkup"),
    ]

    # Appointment status tracking
    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    # User who scheduled the appointment
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    # Pet for which appointment is scheduled
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    # Type of appointment
    appointment_type = models.CharField(
        max_length=50,
        choices=APPOINTMENT_TYPE_CHOICES
    )

    # Appointment date and time
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    # Clinic or hospital name
    clinic = models.CharField(
        max_length=100
    )

    # Optional notes for appointment
    notes = models.TextField(
        blank=True
    )

    # Current appointment status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Scheduled"
    )

    # Timestamp when record is created
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        # Shows appointment summary
        return f"{self.pet.name} - {self.appointment_type} ({self.appointment_date})"


# medication page:
class Medication(models.Model):
    # Owner of medication schedule
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Pet receiving the medication
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    # Medication details
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)      # e.g. 5ml, 1 tablet
    frequency = models.CharField(max_length=50)   # e.g. Twice a day

    # Medication duration
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    # Optional notes
    notes = models.TextField(blank=True)

    # Auto timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Displays medication with pet name
        return f"{self.medication_name} - {self.pet.name}"


# setting page:
class UserSettings(models.Model):
    # One-to-one relationship ensures one settings record per user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Notification preferences
    email_notifications = models.BooleanField(default=True)
    appointment_reminders = models.BooleanField(default=True)
    medication_reminders = models.BooleanField(default=True)

    # UI preference
    dark_mode = models.BooleanField(default=False)

    def __str__(self):
        # Shows which user's settings are displayed
        return f"Settings for {self.user.username}"
