
# Create your views here.
from Category import views
from django.shortcuts import render
from .models import Category
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def category_home(request):
    categories = Category.objects.all()
    return render(request, 'category_home.html', {'categories': categories})



def add_category(request):
    if request.method == 'POST':
        # Get data from the form submission
        name = request.POST['name']
        tot_bag = request.POST['tot_bag']
        bag_wei = request.POST['bag_wei']
        tot_wei = request.POST['tot_wei']

        # Create a new Category object and save it to the database
        category = Category(name=name, tot_bag=tot_bag, bag_wei=bag_wei, tot_wei=tot_wei)
        category.save()

        # Success message and redirect after saving
        messages.success(request, "Category added successfully!")
        return redirect('category_home01')  # Redirect to the category home page
    
    # Render the form to add a new category if GET request
    return render(request, 'add_category.html')


def update_category(request, category_id):
    # Fetch the category instance by ID
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        # Get updated data from the form
        category.name = request.POST.get('name')
        category.tot_bag = request.POST.get('tot_bag')
        category.bag_wei = request.POST.get('bag_wei')
        category.tot_wei = request.POST.get('tot_wei')
        
        # Save the updated category
        category.save()
        
        return redirect('category_home01')  # Redirect to the category home page after update
    
    # If it's a GET request, render the form with existing category data
    return render(request, 'update_category.html', {'category': category})


def delete_category(request, category_id):
    ##Fetch the category instance by ID
    category = get_object_or_404(Category, id=category_id)
    
    # Delete the category
    category.delete()
    
    #messages.success(request, "Category deleted successfully!")
    return redirect('category_home01') 


