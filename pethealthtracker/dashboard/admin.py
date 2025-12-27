from django.contrib import admin
# Register your models here.
from .models import (
    Pet,
    HealthRecord,
    Appointment,
    Medication,
    UserSettings,
)
admin.site.register(Pet)
admin.site.register(HealthRecord)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(UserSettings)
