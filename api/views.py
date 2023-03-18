from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Assistant, UserProfile, Patient, Treatment

def home(request):
    user_role = None
    user_obj = None
    
    if request.user.is_authenticated:
        try:
            user_obj = UserProfile.objects.get(user=request.user)
            user_role = user_obj.role
        except UserProfile.DoesNotExist:
            pass
    
    context = {}
    if user_role == 'doctor' or user_role == 'general_manager':
        context['profile'] = user_obj
    elif user_role == 'assistant':
        context['assistant'] = Assistant.objects.get(user=request.user)
    else:
        context['guest'] = True
        
    return render(request, 'home.html', context)


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