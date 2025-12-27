from django.urls import path
from . import views
# Imports Django path function and dashboard app views

app_name = "dashboard"
# Namespace for dashboard URLs to avoid name conflicts
# Used in templates like: {% url 'dashboard:index' %}


urlpatterns = [
     
    #dashboard home page:
    # Displays dashboard overview with stats and quick actions
    path("", views.dashboard_view, name="index"),


    # mypets page:
    # Lists all pets belonging to the logged-in user
    path("pets/", views.my_pets_view, name="mypets"),

    #create pet profile page:
    # Form to add a new pet profile
    path("pets/create/", views.create_pet_view, name="create_pet"),

    #edit pet:
    # Updates an existing pet profile using pet ID
    path("pets/edit/<int:pet_id>/", views.edit_pet_view, name="edit_pet"),

    #delete pet:
    # Deletes a pet record securely using pet ID
    path("pets/delete/<int:pet_id>/", views.delete_pet_view, name="delete_pet"),


    #healthrecords page: 
    # Shows vaccination and health history of pets
    path("health-records/", views.health_records_view, name="health_records"),

    # add healthrecords page:
    # Form to add a new health or vaccination record
    path("health-records/add/", views.create_health_record_view, name="add_health_record"),

    #edit healthrecord:
    # Edits an existing health record using record ID
    path("health-records/edit/<int:record_id>/", views.edit_health_record_view, name="edit_health_record"),

    #delete healthrecord:
    # Deletes a health record entry
    path("health-records/delete/<int:record_id>/", views.delete_health_record_view, name="delete_health_record"),


    #appointment page:
    # Displays all scheduled appointments for the user
    path("appointments/", views.appointments_view, name="appointments"),

    # schedule apoointment page:
    # Form to schedule a new appointment
    path("appointments/add/", views.create_appointment_view, name="add_appointment"),

    #edit appointment:
    # Updates appointment details using appointment ID
    path("appointments/edit/<int:appointment_id>/", views.edit_appointment_view, name="edit_appointment"),

    #delete appointment:
    # Cancels or deletes an appointment
    path("appointments/delete/<int:appointment_id>/", views.delete_appointment_view, name="delete_appointment"),


    # medication page:
    # Displays medication schedules for pets
    path("medications/", views.medications_view, name="medications"),

    # add medication page:
    # Form to add a new medication schedule
    path("medications/add/", views.create_medication_view, name="add_medication"),

    #edit medication:
    # Updates medication details using medication ID
    path("medications/edit/<int:medication_id>/", views.edit_medication_view, name="edit_medication"),

    #delete medication:
    # Deletes a medication entry
    path("medications/delete/<int:medication_id>/", views.delete_medication_view, name="delete_medication"),


    #profile page:
    # Displays and updates logged-in user profile
    path("profile/", views.profile_view, name="profile"),


    #setting page:
    # Allows users to manage notification and UI preferences
    path("settings/", views.settings_view, name="settings"),

]
