from django.shortcuts import redirect, render
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required
from .models import Pet
from django.shortcuts import get_object_or_404


@login_required(login_url="/login/")
def dashboard_view(request):
    pets_count = Pet.objects.filter(owner=request.user).count()
    
    return render(request, "dashboard/index.html", {
        "pets_count": pets_count
    })


@login_required(login_url="login")
def create_pet_view(request):
    if request.method == "POST":
        Pet.objects.create(
            owner=request.user,
            name=request.POST.get("name"),
            pet_type=request.POST.get("pet_type"),
            breed=request.POST.get("breed"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            weight=request.POST.get("weight"),
        )
        return redirect("dashboard:mypets")

    return render(request, "dashboard/create_pet.html")

@login_required(login_url="login")
def my_pets_view(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "dashboard/mypets.html", {"pets": pets})

@login_required(login_url="login")
def edit_pet_view(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)

    if request.method == "POST":
        pet.name = request.POST.get("name")
        pet.pet_type = request.POST.get("pet_type")
        pet.breed = request.POST.get("breed")
        pet.age = request.POST.get("age")
        pet.gender = request.POST.get("gender")
        pet.weight = request.POST.get("weight")
        pet.save()

        return redirect("dashboard:mypets")

    return render(request, "dashboard/edit_pet.html", {"pet": pet})

@login_required(login_url="login")
def delete_pet_view(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)

    if request.method == "POST":
        pet.delete()
        return redirect("dashboard:mypets")

    return render(request, "dashboard/delete_pet.html", {"pet": pet})