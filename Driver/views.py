

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Driver
from Driver.models import LogisticUser

def homepage_driver(request):
    drivers = LogisticUser.objects.all()
    return render(request,"driver_home.html",{"drivers":drivers})



def add_driver(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if 'license' in request.FILES:
            license = request.FILES['license']
        else:
            messages.error(request, "Please upload a valid license image.")
            return redirect('driver_add')

        # Save the driver object
        driver = LogisticUser(
            name=name,
            mobile=mobile,
            email=email,
            liscence=license
        )
        driver.set_password(password)
        driver.save()

        messages.success(request, "Driver added successfully!")
        return redirect('driver_home01')

    return render(request, "add_driver.html")




def update_driver(request, did):
    # Fetch the driver object by primary key (did)
    driver = get_object_or_404(LogisticUser, pk=did)
    
    if request.method == 'POST':
        # Updating the driver object with form data
        driver.name = request.POST['name']
        driver.mobile = request.POST['mobile']
        driver.email = request.POST['email']
        driver.password = request.POST['password']
        
        if 'license' in request.FILES:
            driver.license = request.FILES['license']  # Update the license file if provided
        
        driver.save()  # Save updated information to the database
        
        return redirect('driver_home01')  # Redirect to a page after successful update
    
    return render(request, 'update_driver.html', {'driver': driver})




def delete_driver(request, did):
    driver = get_object_or_404(Driver, pk=did)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_home01')  # Redirect to a list or home page after deletion
    return render(request, 'confirm_delete.html', {'driver': driver})



#trip form 
