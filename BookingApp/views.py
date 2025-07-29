from django.shortcuts import render
from django.http import HttpResponse
from .myforms import SignupForm
from django.shortcuts import redirect
# Create your views here.

def login(request):
    return render(request, 'BookingApp\login.html')

def register(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.is_superuser = False  # Set as superuser
            user.is_staff = False  # Required for admin access
            user.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = SignupForm()
    return render(request, 'BookingApp/register.html' , {'form':form})