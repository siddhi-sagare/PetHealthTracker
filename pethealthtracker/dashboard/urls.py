from django.urls import path
from . import views

app_name = "dashboard"


urlpatterns = [

     path("", views.dashboard_view, name="index"),
     path("pets/", views.my_pets_view, name="mypets"),
     path("pets/create/", views.create_pet_view, name="create_pet"),

     # NEW
    path("pets/edit/<int:pet_id>/", views.edit_pet_view, name="edit_pet"),
    path("pets/delete/<int:pet_id>/", views.delete_pet_view, name="delete_pet"),

    path("health-records/add/",views.create_health_record_view,name="add_health_record"),
    path("health-records/",views.health_records_view,name="health_records"),
    path("health-records/edit/<int:record_id>/",views.edit_health_record_view,name="edit_health_record"),
    path("health-records/delete/<int:record_id>/",views.delete_health_record_view,name="delete_health_record"),

    path("appointments/add/",views.create_appointment_view,name="add_appointment"),
    path("appointments/",views.appointments_view,name="appointments"),
    path("appointments/edit/<int:appointment_id>/",views.edit_appointment_view,name="edit_appointment"),
    path("appointments/delete/<int:appointment_id>/",views.delete_appointment_view,name="delete_appointment"),

    path("medications/add/",views.create_medication_view,name="add_medication"),
    path("medications/",views.medications_view,name="medications"),
    path("medications/edit/<int:medication_id>/",views.edit_medication_view,name="edit_medication"),
    path("medications/delete/<int:medication_id>/",views.delete_medication_view,name="delete_medication"),

    path("profile/", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),


    
]