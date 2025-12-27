from django.urls import path
from . import views

app_name = "dashboard"


urlpatterns = [
     
    #dashboard home page:
    path("", views.dashboard_view, name="index"),


    # mypets page:
    path("pets/", views.my_pets_view, name="mypets"),
    #create pet profile page:
    path("pets/create/", views.create_pet_view, name="create_pet"),
    #edit pet:
    path("pets/edit/<int:pet_id>/", views.edit_pet_view, name="edit_pet"),
    #delete pet:
    path("pets/delete/<int:pet_id>/", views.delete_pet_view, name="delete_pet"),


    #healthrecords page: 
    path("health-records/",views.health_records_view,name="health_records"),
    # add healthrecords page:
    path("health-records/add/",views.create_health_record_view,name="add_health_record"),
    #edit healthrecord:
    path("health-records/edit/<int:record_id>/",views.edit_health_record_view,name="edit_health_record"),
    #delete healthrecord:
    path("health-records/delete/<int:record_id>/",views.delete_health_record_view,name="delete_health_record"),


    #appointment page:
    path("appointments/",views.appointments_view,name="appointments"),
    # schedule apoointment page:
    path("appointments/add/",views.create_appointment_view,name="add_appointment"),
    #edit appointment:
    path("appointments/edit/<int:appointment_id>/",views.edit_appointment_view,name="edit_appointment"),
    #delete appointment:
    path("appointments/delete/<int:appointment_id>/",views.delete_appointment_view,name="delete_appointment"),


    # medication page:
    path("medications/",views.medications_view,name="medications"),
    # add medication page:
    path("medications/add/",views.create_medication_view,name="add_medication"),
    #edit medication:
    path("medications/edit/<int:medication_id>/",views.edit_medication_view,name="edit_medication"),
    #delete medication:
    path("medications/delete/<int:medication_id>/",views.delete_medication_view,name="delete_medication"),


    #profile page:
    path("profile/", views.profile_view, name="profile"),


    #setting page:
    path("settings/", views.settings_view, name="settings"),

]