from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Imports Django authentication utilities and User model


# landing/main home page:
def index(request):
    # Renders the public landing page
    return render(request, 'home/index.html')


# features page:
def features(request):
    # Displays application features overview
    return render(request, 'home/features.html')


# how it works page:
def how_it_works(request):
    # Explains step-by-step usage of the application
    return render(request, 'home/how_it_works.html')


# contact us page:
def contact(request):
    # Displays contact information or contact form
    return render(request, 'home/contact.html')


# login page:
def login_view(request):
    # Handles user authentication
    if request.method == "POST":
        # Retrieves credentials from login form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticates user using Django's auth system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Logs in the user and creates session
            login(request, user)

            # Redirects authenticated user to dashboard
            return redirect('dashboard:index')
        else:
            # Displays error message for invalid credentials
            return render(request, "home/login.html", {
                "error": "Invalid username or password"
            })

    # Displays login page for GET request
    return render(request, "home/login.html")


# register page:
def register_view(request):
    # Handles new user registration
    if request.method == "POST":
        # Collects registration form data
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Checks if passwords match
        if password1 != password2:
            return render(request, "home/register.html", {
                "error": "Passwords do not match"
            })

        # Checks if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "home/register.html", {
                "error": "Username already exists"
            })

        # Creates a new user account securely
        User.objects.create_user(
            username=username,
            password=password1,
            email=email,
        )

        # Redirects user to login page after successful registration
        return redirect("login")   # Register → Login

    # Displays registration page for GET request
    return render(request, "home/register.html")


# logout page:
def logout_view(request):
    # Logs out the current user and clears session
    logout(request)

    # Redirects to home page after logout
    return redirect('home')
