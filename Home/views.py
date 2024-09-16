
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Driver.models import LogisticUser
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DriverForm 
# from Driver.views import driver_homepage



def user_login(request):
    if request.method == "POST":
        email = request.POST.get('username').lower()  # Convert to lowercase for case-insensitive comparison
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')
        
        print(email, password, usertype)
        try:
            # import pdb; pdb.set_trace()
            #check the user type
            if usertype == "admin":
                user = LogisticUser.objects.get(email=email, user_type='admin')
                if user.check_password(password):
                    return render(request, "admin_homepage.html",{'email': user.email})
                
                
            else:
                user = LogisticUser.objects.get(email=email, user_type='driver')
                print(user)
                if user.check_password(password):
                    return render(request, "driver_homepage.html", {'email': user.email})

        except LogisticUser.DoesNotExist:
            messages.error(request, "username or password is invalid!")
    
    return render(request, "login.html")



#admin-home page

def admin_home(request):
    return render(request, 'admin_homepage.html')



#driver-login

def driver_home(request):
    return render(request, 'driver_homepage.html')



