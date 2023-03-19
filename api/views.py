from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Assistant, UserProfile, Patient, Treatment

def home(request): 
    return render(request, 'home.html')

def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,f'User {username} does not exist!')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,f'Username or password are incorrect!')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def view_doctors(request):
    return render(request, 'doctors.html')

def view_doctor(request, pk):
    return render(request, 'doctors.html')

def view_assistants(request):
    return render(request, 'assistants.html')

def view_assistant(request, pk):
    return render(request, 'assistants.html')

def view_patients(request):
    return render(request, 'patients.html')

def view_patient(request, pk):
    return render(request, 'patients.html')

def view_treatments(request):
    return render(request, 'treatments.html')