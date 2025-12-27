"""
URL configuration for pethealthtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
# Imports Django admin, URL utilities, and built-in auth views


urlpatterns = [

    # main admin panel:
    # Provides Django's default admin interface for managing models
    path('admin/', admin.site.urls),

    # homeapp:
    # Handles public-facing pages such as home, login, register, features, contact
    path('', include('home.urls')), 

    # dashboardapp:
    # Handles authenticated user dashboard features
    # Includes pets, health records, appointments, medications, profile, and settings
    path('dashboard/', include('dashboard.urls')), 

    # Provides login, logout, password reset, password change 
    # Uses Django’s built-in authentication URL patterns
    # Example URLs:
    # /accounts/login/
    # /accounts/logout/
    # /accounts/password_change/
    # /accounts/password_reset/
    # path("accounts/", include("django.contrib.auth.urls")),

    # in dashboardapp in my profile page( customize password change ):
    # Overrides Django’s default password change behavior
    # After successful password change, user is redirected to dashboard profile page
    # NOTE: This path should be placed ABOVE the "accounts/" include
    # if you want it to fully override Django’s default password_change URL
    path(
        "accounts/password/change/",
        auth_views.PasswordChangeView.as_view(
            success_url="/dashboard/profile/"
        ),
        name="password_change",
    ),

]

