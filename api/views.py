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
    doctors = UserProfile.objects.filter(role='doctor')
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)
    
def view_doctor(request, pk):
    doctor = UserProfile.objects.get(user__id=pk, role='doctor')
    context = {'doctor': doctor}
    return render(request, 'doctor.html', context)

def view_assistants(request):
    assistants = Assistant.objects.all()
    context = {'assistants': assistants}
    return render(request, 'assistants.html', context)

def view_assistant(request, pk):
    assistant = Assistant.objects.get(id=pk)
    context = {'assistant': assistant}
    return render(request, 'assistant.html', context)

def view_patients(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patients.html', context)

def view_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient': patient}
    return render(request, 'patient.html', context)

def view_treatments(request):
    treatments = Treatment.objects.all()
    context = {'treatments': treatments}
    return render(request, 'treatments.html', context)


def view_treatment(request, pk):
    treatment = Treatment.objects.get(id=pk)
    context = {'treatment': treatment}
    return render(request, 'treatment.html', context)