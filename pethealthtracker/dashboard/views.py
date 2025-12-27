from django.shortcuts import redirect, render
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required
from .models import Pet, HealthRecord, Appointment, Medication,UserSettings
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required


# dashboard home page:
@login_required(login_url="/login/")
def dashboard_view(request):
    pets_count = Pet.objects.filter(owner=request.user).count()
    health_records_count = HealthRecord.objects.filter(owner=request.user).count()
    appointments_count = Appointment.objects.filter(owner=request.user).count()
    medications_count = Medication.objects.filter(owner=request.user).count()
    return render(
        request,
        "dashboard/index.html",
        {
            "pets_count": pets_count,
            "health_records_count": health_records_count,
            "appointments_count": appointments_count,
            "medications_count": medications_count,
        }
    )


# create pet profile page:
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


# mypets page:
@login_required(login_url="login")
def my_pets_view(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "dashboard/mypets.html", {"pets": pets})


# edit pet:
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


# delete pet:
@login_required(login_url="login")
def delete_pet_view(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    if request.method == "POST":
        pet.delete()
        return redirect("dashboard:mypets")
    return render(request, "dashboard/delete_pet.html", {"pet": pet})


# add healthrecord page:
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


# healthrecords page:
@login_required(login_url="login")
def health_records_view(request):
    records = HealthRecord.objects.filter(owner=request.user)
    return render(
        request,
        "dashboard/health_records.html",
        {"records": records}
    )


# edit healthrecord:
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


# delete healthrecord:
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


# scedule appointment page:
@login_required(login_url="login")
def create_appointment_view(request):
    pets = Pet.objects.filter(owner=request.user)
    if request.method == "POST":
        Appointment.objects.create(
            owner=request.user,
            pet_id=request.POST.get("pet"),
            appointment_type=request.POST.get("appointment_type"),
            appointment_date=request.POST.get("appointment_date"),
            appointment_time=request.POST.get("appointment_time"),
            clinic=request.POST.get("clinic"),
            notes=request.POST.get("notes"),
        )
        return redirect("dashboard:appointments")
    return render(
        request,
        "dashboard/create_appointment.html",
        {"pets": pets}
    )


# appointment page:
@login_required(login_url="login")
def appointments_view(request):
    appointments = Appointment.objects.filter(owner=request.user)
    return render(
        request,
        "dashboard/appointments.html",
        {"appointments": appointments}
    )


# edit appointment
@login_required(login_url="login")
def edit_appointment_view(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        owner=request.user
    )
    pets = Pet.objects.filter(owner=request.user)
    if request.method == "POST":
        appointment.pet_id = request.POST.get("pet")
        appointment.appointment_type = request.POST.get("appointment_type")
        appointment.appointment_date = request.POST.get("appointment_date")
        appointment.appointment_time = request.POST.get("appointment_time")
        appointment.clinic = request.POST.get("clinic")
        appointment.notes = request.POST.get("notes")
        appointment.save()
        return redirect("dashboard:appointments")
    return render(
        request,
        "dashboard/edit_appointment.html",
        {
            "appointment": appointment,
            "pets": pets
        }
    )


# delete appointment:
@login_required(login_url="login")
def delete_appointment_view(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        owner=request.user
    )
    if request.method == "POST":
        appointment.delete()
    return redirect("dashboard:appointments")


# add medication page:
@login_required(login_url="login")
def create_medication_view(request):
    pets = Pet.objects.filter(owner=request.user)
    if request.method == "POST":
        Medication.objects.create(
            owner=request.user,
            pet_id=request.POST.get("pet"),
            medication_name=request.POST.get("medication_name"),
            dosage=request.POST.get("dosage"),
            frequency=request.POST.get("frequency"),
            start_date=request.POST.get("start_date"),
            end_date=request.POST.get("end_date") or None,
            notes=request.POST.get("notes"),
        )
        return redirect("dashboard:medications")
    return render(
        request,
        "dashboard/create_medication.html",
        {"pets": pets}
    )


# medication page:
@login_required(login_url="login")
def medications_view(request):
    medications = Medication.objects.filter(owner=request.user)
    return render(
        request,
        "dashboard/medications.html",
        {"medications": medications}
    )


# edit medication:
@login_required(login_url="login")
def edit_medication_view(request, medication_id):
    medication = get_object_or_404(
        Medication,
        id=medication_id,
        owner=request.user
    )
    pets = Pet.objects.filter(owner=request.user)
    if request.method == "POST":
        medication.pet_id = request.POST.get("pet")
        medication.medication_name = request.POST.get("medication_name")
        medication.dosage = request.POST.get("dosage")
        medication.frequency = request.POST.get("frequency")
        medication.start_date = request.POST.get("start_date")
        medication.end_date = request.POST.get("end_date") or None
        medication.notes = request.POST.get("notes")
        medication.save()
        return redirect("dashboard:medications")
    return render(
        request,
        "dashboard/edit_medication.html",
        {
            "medication": medication,
            "pets": pets
        }
    )


# delete medication:
@login_required(login_url="login")
def delete_medication_view(request, medication_id):
    medication = get_object_or_404(
        Medication,
        id=medication_id,
        owner=request.user
    )
    if request.method == "POST":
        medication.delete()
    return redirect("dashboard:medications")


# profile page:
@login_required(login_url="/login/")
def profile_view(request):
    if request.method == "POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("dashboard:profile")
    return render(request, "dashboard/profile.html")


# settings page:
@login_required(login_url="/login/")
def settings_view(request):
    # get or create settings for this user
    settings, created = UserSettings.objects.get_or_create(
        user=request.user
    )
    if request.method == "POST":
        settings.email_notifications = bool(
            request.POST.get("email_notifications")
        )
        settings.appointment_reminders = bool(
            request.POST.get("appointment_reminders")
        )
        settings.medication_reminders = bool(
            request.POST.get("medication_reminders")
        )
        settings.dark_mode = bool(
            request.POST.get("dark_mode")
        )

        settings.save()
        return redirect("dashboard:settings")
    return render(request, "dashboard/settings.html", {
        "settings": settings
    }
    )



