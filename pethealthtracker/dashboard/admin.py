from django.contrib import admin
# Imports Django's built-in admin module

# Importing models to make them manageable via admin panel
from .models import (
    Pet,            # Stores pet profile information
    HealthRecord,   # Stores vaccination and health records of pets
    Appointment,    # Stores vet appointment details
    Medication,     # Stores medication schedules for pets
    UserSettings,   # Stores user-specific application settings
)

# Registering models with Django admin site
# This allows admin users to perform CRUD operations from admin dashboard

admin.site.register(Pet)            # Register Pet model
admin.site.register(HealthRecord)   # Register HealthRecord model
admin.site.register(Appointment)    # Register Appointment model
admin.site.register(Medication)     # Register Medication model
admin.site.register(UserSettings)   # Register UserSettings model
