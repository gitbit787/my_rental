from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm
from .models import Renter, Property


# Create your views here.
def home(request):
     context = {'title': 'Home' }
     return render(request, 'home.html', context)

def signup(request):
    properties = Property.objects.filter(available=True)
    properties_data = {
        str(prop.property_id): {
            'name': prop.name,
            'address': prop.address,
            'unit': prop.unit,
            'city': prop.city,
            'state': prop.state,
            'zip_code': prop.zip_code,
            'country': prop.country
        }
        for prop in properties
    }
    
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            selected_property = form.cleaned_data['property']
            user = form.save()
            # Create Renter record linked to user with property address
            renter = Renter.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=selected_property.address,
                unit=selected_property.unit,
                city=selected_property.city,
                state=selected_property.state,
                zip_code=selected_property.zip_code,
                country=selected_property.country
            )
            login(request, user)
            return redirect('home')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form, 'properties_data': properties_data})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid username or password. Please try again."
        else:
            error_message = "Invalid username or password. Please try again."
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

@login_required
def profile(request):
    try:
        renter = Renter.objects.get(user=request.user)
    except Renter.DoesNotExist:
        renter = None
    return render(request, 'profile.html', {'renter': renter})

def logout_view(request):
    logout(request)
    return redirect('home')
