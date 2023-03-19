from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Assistant, UserProfile, Patient, Treatment, RoleChoices
from .forms import AssistantForm, PatientForm, DoctorForm

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

def doctor_register(request):
    form = DoctorForm()

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            user_profile = UserProfile(user=user, role= RoleChoices.DOCTOR)
            user_profile.save()
            return redirect('doctors')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'doctor_register.html', {'form': form})

def doctor_update(request,pk):
    pass

def assistant_register(request):
    form = AssistantForm()

    if request.method == 'POST':
        form = AssistantForm(request.POST)
        if form.is_valid():
            assistant = form.save(commit=False)
            assistant.username = assistant.username.lower()
            assistant.save()
            
            return redirect('assistants')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'assistant_register.html', {'form': form})

def assistant_update(request,pk):
    pass

def patient_register(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            
            return redirect('patients')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'patient_register.html', {'form': form})

def patient_update(request,pk):
    pass