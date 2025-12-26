from django.shortcuts import redirect, render
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required
from .models import Pet, HealthRecord
from django.shortcuts import get_object_or_404


@login_required(login_url="/login/")
def dashboard_view(request):
    pets_count = Pet.objects.filter(owner=request.user).count()
    health_records_count = HealthRecord.objects.filter(owner=request.user).count()

    return render(
        request,
        "dashboard/index.html",
        {
            "pets_count": pets_count,
            "health_records_count": health_records_count,
        }
    )



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


@login_required(login_url="login")
def create_health_record_view(request):
    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        HealthRecord.objects.create(
            owner=request.user,
            pet_id=request.POST.get("pet"),
            event_type=request.POST.get("event_type"),
            event_date=request.POST.get("event_date"),
            description=request.POST.get("description"),
            veterinarian=request.POST.get("veterinarian"),
        )
        return redirect("dashboard:health_records")

    return render(
        request,
        "dashboard/create_health_record.html",
        {"pets": pets}
    )

@login_required(login_url="login")
def health_records_view(request):
    records = HealthRecord.objects.filter(owner=request.user)
    return render(
        request,
        "dashboard/health_records.html",
        {"records": records}
    )

@login_required(login_url="login")
def edit_health_record_view(request, record_id):
    record = get_object_or_404(
        HealthRecord,
        id=record_id,
        owner=request.user
    )

    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        record.pet_id = request.POST.get("pet")
        record.event_type = request.POST.get("event_type")
        record.event_date = request.POST.get("event_date")
        record.description = request.POST.get("description")
        record.veterinarian = request.POST.get("veterinarian")
        record.save()

        return redirect("dashboard:health_records")

    return render(
        request,
        "dashboard/edit_health_record.html",
        {
            "record": record,
            "pets": pets
        }
    )

@login_required(login_url="login")
def delete_health_record_view(request, record_id):
    record = get_object_or_404(
        HealthRecord,
        id=record_id,
        owner=request.user
    )

    if request.method == "POST":
        record.delete()
        return redirect("dashboard:health_records")

    return render(
        request,
        "dashboard/delete_health_record.html",
        {"record": record}
    )