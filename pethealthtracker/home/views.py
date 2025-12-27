from django.shortcuts import redirect, render


from django.contrib.auth import authenticate, login,logout
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
            return redirect('dashboard:index')   # ✅ redirect to dashboard
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "home/login.html")


# def register_view(request):
#     return render(request, 'home/register.html')


from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "home/register.html", {
                "error": "Passwords do not match"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "home/register.html", {
                "error": "Username already exists"
            })

        # ✅ Create user
        User.objects.create_user(
            username=username,
            password=password1,
           email=email, 
        )

        return redirect("login")   # ✅ Register → Login

    return render(request, "home/register.html")

def logout_view(request):
    logout(request)
    return redirect('home')