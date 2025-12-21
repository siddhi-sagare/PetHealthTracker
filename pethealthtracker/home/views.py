from django.shortcuts import redirect, render


from django.contrib.auth import authenticate, login
def index(request):
    return render(request, 'home/index.html')

def features(request):
    return render(request, 'home/features.html')

def how_it_works(request):
    return render(request, 'home/how_it_works.html')

def contact(request):
    return render(request, 'home/contact.html')

# 



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")   # ✅ redirect to dashboard
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "home/login.html")


def register_view(request):
    return render(request, 'home/register.html')

