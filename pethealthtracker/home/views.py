from django.shortcuts import render





def index(request):
    return render(request, 'home/index.html')

def features(request):
    return render(request, 'home/features.html')

def how_it_works(request):
    return render(request, 'home/how_it_works.html')

def contact(request):
    return render(request, 'home/contact.html')

def login_view(request):
    return render(request, 'home/login.html')

def register_view(request):
    return render(request, 'home/register.html')

