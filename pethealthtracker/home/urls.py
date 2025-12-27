from django.urls import path
from . import views
# Imports Django path function and views from home app


urlpatterns = [

    # landing/main home page:
    # Displays the public landing page of the website
    # Shows intro, features preview, and call-to-action
    path('', views.index, name='home'),

    # features page:
    # Displays detailed features of the Pet Health Tracker
    path('features/', views.features, name='features'),

    # how it works page:
    # Explains step-by-step usage of the application
    path('howitworks/', views.how_it_works, name='how_it_works'),

    # contact us page:
    # Provides contact form or contact information
    path('contact/', views.contact, name='contact'),
    
    # register page:
    # Handles new user registration
    path('register/', views.register_view, name='register'),

    # login page:
    # Authenticates existing users and redirects to dashboard
    path("login/", views.login_view, name="login"),

    # logout page:
    # Logs out the current user and redirects to home/login page
    path('logout/', views.logout_view, name='logout'),

]
