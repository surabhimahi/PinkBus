from django.shortcuts import render
from django.http import HttpResponse
from .myforms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .models import Route, Schedule, Bus, Seat
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        buses = Bus.objects.filter(start_route__name=start, end_route__name=end)
        if not buses:   
            messages.error(request, 'No buses found for the selected routes.') 
        return render(request, "BookingApp/home.html", {"buses": buses, "start": start, "end": end})
    
    else:
        cities = Route.objects.all()
    return render(request, "BookingApp/home.html", {"cities": cities})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if User.objects.filter(username=username).exists():
              
                user = authenticate(request, username=username, password=password)
                if user is not None:
         
                    login(request, user)
                    return redirect('homeview')  
                else: 
                    print("yess")
                    messages.error(request, 'Enter correct username and password.')
            else: 
                messages.error(request, 'Username not found. Kindly sign up.')
    else:
        form = LoginForm() 
    return render(request, 'BookingApp/login.html', {'form': form})

def register(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.is_superuser = False  # Set as superuser
            user.is_staff = False  # Required for admin access
            user.save()
            return redirect('login_view')  # Redirect to login after successful signup
    else:
        form = SignupForm()
    return render(request, 'BookingApp/register.html' , {'form':form})