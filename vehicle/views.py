
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import vehicle


def homepage_vehicle(request):
    vehicles = vehicle.objects.all()
    return render(request,"vehicle_home.html",{"vehicles":vehicles})


def add_vehicle(request):
    if request.method == "POST":
        v_name = request.POST.get("v_name")
        v_number = request.POST.get("v_number")
        c_number = request.POST.get("c_number")
        v_photo = request.POST.get("v_photo")
        
        if 'v_photo' in request.FILES:
            v_photo = request.FILES['v_photo']
        else:
            messages.error(request, "Please upload a valid license image.")
            return redirect('driver_add')

        # Save the driver object
        Vehicle = vehicle(
            v_name=v_name,
            v_number=v_number,
            c_number=c_number,
            v_photo=v_photo
        )
        Vehicle.save()

        messages.success(request, "Vehicle added successfully!")
        return redirect('vehicle_home01')

    return render(request, "add_vehicle.html")


def delete_vehicle(request, vehicle_id):
    # Fetch the vehicle instance by ID
    vehicle_instance = get_object_or_404(vehicle, id=vehicle_id)
    
    # Delete the vehicle
    vehicle_instance.delete()
    
    # Success message after deletion
    messages.success(request, "Vehicle deleted successfully!")
    
    # Redirect to the vehicle home page
    return redirect('vehicle_home01')


def update_vehicle(request, vehicle_id):
    # Get the vehicle instance by ID or return a 404 error if not found
    vehicle_instance = get_object_or_404(vehicle, id=vehicle_id)

    if request.method == "POST":
        v_name = request.POST.get("v_name")
        v_number = request.POST.get("v_number")
        c_number = request.POST.get("c_number")
        
        # Check if a new photo has been uploaded
        if 'v_photo' in request.FILES:
            v_photo = request.FILES['v_photo']
            vehicle_instance.v_photo = v_photo  # Update the photo field

        # Update the vehicle instance with the new data
        vehicle_instance.v_name = v_name
        vehicle_instance.v_number = v_number
        vehicle_instance.c_number = c_number

        # Save the updated vehicle instance
        vehicle_instance.save()

        # Success message after update
        messages.success(request, "Vehicle updated successfully!")
        return redirect('vehicle_home01')

    # Pre-populate the form with the existing vehicle data
    return render(request, "update_vehicle.html", {"vehicle": vehicle_instance})