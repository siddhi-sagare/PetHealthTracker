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
]