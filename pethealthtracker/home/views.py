from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def features(request):
    return render(request, 'home/features.html')

def how_it_works(request):
    return render(request, 'home/how_it_works.html')

def contact(request):
    return render(request, 'home/contact.html')

def login(request):
    return render(request, 'home/login.html')

def register(request):
    return render(request, 'home/register.html')