from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

# Importing application models
from .models import Pet, HealthRecord, Appointment, Medication, UserSettings
# These models represent core entities of the dashboard module


# dashboard home page:
@login_required(login_url="/login/")
def dashboard_view(request):
    # Fetches count of related objects for logged-in user
    # Used to display dashboard statistics
    pets_count = Pet.objects.filter(owner=request.user).count()
    health_records_count = HealthRecord.objects.filter(owner=request.user).count()
    appointments_count = Appointment.objects.filter(owner=request.user).count()
    medications_count = Medication.objects.filter(owner=request.user).count()

    # Renders dashboard overview page with statistics
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
    # Handles pet creation form submission
    if request.method == "POST":
        # Creates a new Pet linked to the logged-in user
        Pet.objects.create(
            owner=request.user,
            name=request.POST.get("name"),
            pet_type=request.POST.get("pet_type"),
            breed=request.POST.get("breed"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            weight=request.POST.get("weight"),
        )
        # Redirects to pet listing page after successful creation
        return redirect("dashboard:mypets")

    # Displays empty pet creation form
    return render(request, "dashboard/create_pet.html")


# mypets page:
@login_required(login_url="login")
def my_pets_view(request):
    # Retrieves all pets owned by the logged-in user
    pets = Pet.objects.filter(owner=request.user)

    # Renders pets listing page
    return render(request, "dashboard/mypets.html", {"pets": pets})


# edit pet:
@login_required(login_url="login")
def edit_pet_view(request, pet_id):
    # Retrieves pet safely and ensures ownership
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)

    if request.method == "POST":
        # Updates pet details
        pet.name = request.POST.get("name")
        pet.pet_type = request.POST.get("pet_type")
        pet.breed = request.POST.get("breed")
        pet.age = request.POST.get("age")
        pet.gender = request.POST.get("gender")
        pet.weight = request.POST.get("weight")
        pet.save()

        # Redirects back to pet list
        return redirect("dashboard:mypets")

    # Displays pet edit form
    return render(request, "dashboard/edit_pet.html", {"pet": pet})


# delete pet:
@login_required(login_url="login")
def delete_pet_view(request, pet_id):
    # Securely fetches pet for deletion
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)

    if request.method == "POST":
        # Deletes pet record
        pet.delete()
        return redirect("dashboard:mypets")

    # Confirmation page before deletion
    return render(request, "dashboard/delete_pet.html", {"pet": pet})


# add healthrecord page:
@login_required(login_url="login")
def create_health_record_view(request):
    # Retrieves pets for dropdown selection
    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        # Creates a new health record entry
        HealthRecord.objects.create(
            owner=request.user,
            pet_id=request.POST.get("pet"),
            event_type=request.POST.get("event_type"),
            event_date=request.POST.get("event_date"),
            description=request.POST.get("description"),
            veterinarian=request.POST.get("veterinarian"),
        )
        return redirect("dashboard:health_records")

    # Displays health record creation form
    return render(
        request,
        "dashboard/create_health_record.html",
        {"pets": pets}
    )


# healthrecords page:
@login_required(login_url="login")
def health_records_view(request):
    # Retrieves all health records for logged-in user
    records = HealthRecord.objects.filter(owner=request.user)

    # Displays health record list
    return render(
        request,
        "dashboard/health_records.html",
        {"records": records}
    )


# edit healthrecord:
@login_required(login_url="login")
def edit_health_record_view(request, record_id):
    # Retrieves specific health record securely
    record = get_object_or_404(
        HealthRecord,
        id=record_id,
        owner=request.user
    )

    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        # Updates health record details
        record.pet_id = request.POST.get("pet")
        record.event_type = request.POST.get("event_type")
        record.event_date = request.POST.get("event_date")
        record.description = request.POST.get("description")
        record.veterinarian = request.POST.get("veterinarian")
        record.save()

        return redirect("dashboard:health_records")

    # Displays edit health record form
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
    # Retrieves health record safely
    record = get_object_or_404(
        HealthRecord,
        id=record_id,
        owner=request.user
    )

    if request.method == "POST":
        # Deletes the record
        record.delete()

    return redirect("dashboard:health_records")


# scedule appointment page:
@login_required(login_url="login")
def create_appointment_view(request):
    # Retrieves pets for appointment assignment
    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        # Creates appointment entry
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

    # Displays appointment scheduling form
    return render(
        request,
        "dashboard/create_appointment.html",
        {"pets": pets}
    )


# appointment page:
@login_required(login_url="login")
def appointments_view(request):
    # Retrieves all appointments for logged-in user
    appointments = Appointment.objects.filter(owner=request.user)

    # Displays appointments list
    return render(
        request,
        "dashboard/appointments.html",
        {"appointments": appointments}
    )


# edit appointment
@login_required(login_url="login")
def edit_appointment_view(request, appointment_id):
    # Securely retrieves appointment
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        owner=request.user
    )

    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        # Updates appointment details
        appointment.pet_id = request.POST.get("pet")
        appointment.appointment_type = request.POST.get("appointment_type")
        appointment.appointment_date = request.POST.get("appointment_date")
        appointment.appointment_time = request.POST.get("appointment_time")
        appointment.clinic = request.POST.get("clinic")
        appointment.notes = request.POST.get("notes")
        appointment.save()

        return redirect("dashboard:appointments")

    # Displays appointment edit form
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
    # Secure deletion of appointment
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
    # Retrieves pets for medication assignment
    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        # Creates medication schedule
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

    # Displays medication creation form
    return render(
        request,
        "dashboard/create_medication.html",
        {"pets": pets}
    )


# medication page:
@login_required(login_url="login")
def medications_view(request):
    # Retrieves medication schedules for logged-in user
    medications = Medication.objects.filter(owner=request.user)

    return render(
        request,
        "dashboard/medications.html",
        {"medications": medications}
    )


# edit medication:
@login_required(login_url="login")
def edit_medication_view(request, medication_id):
    # Securely retrieves medication record
    medication = get_object_or_404(
        Medication,
        id=medication_id,
        owner=request.user
    )

    pets = Pet.objects.filter(owner=request.user)

    if request.method == "POST":
        # Updates medication details
        medication.pet_id = request.POST.get("pet")
        medication.medication_name = request.POST.get("medication_name")
        medication.dosage = request.POST.get("dosage")
        medication.frequency = request.POST.get("frequency")
        medication.start_date = request.POST.get("start_date")
        medication.end_date = request.POST.get("end_date") or None
        medication.notes = request.POST.get("notes")
        medication.save()

        return redirect("dashboard:medications")

    # Displays medication edit form
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
    # Secure deletion of medication record
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
    # Allows user to update username and email
    if request.method == "POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()

        return redirect("dashboard:profile")

    # Displays profile page
    return render(request, "dashboard/profile.html")


# settings page:
@login_required(login_url="/login/")
def settings_view(request):
    # Retrieves or creates settings record for the user
    settings, created = UserSettings.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        # Updates user preferences
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

    # Displays settings page
    return render(
        request,
        "dashboard/settings.html",
        {"settings": settings}
    )
