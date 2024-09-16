from django.shortcuts import render

# Create your views here.
def homepage_Trip(request):
    trips = Trip.objects.all()
    return render(request,"trip_form.html",{"trips":trips})
