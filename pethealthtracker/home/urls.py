from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('features/', views.features, name='features'),
    path('howitworks/', views.how_it_works, name='how_it_works'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    
]
