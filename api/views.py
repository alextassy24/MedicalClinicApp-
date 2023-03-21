from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Assistant, UserProfile, Patient, Treatment, RoleChoices
from .forms import AssistantForm, PatientForm, DoctorForm, AssistantUpdateForm, PatientUpdateForm, DoctorUpdateForm, TreatmentForm, TreatmentUpdateForm

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
    doctor = User.objects.get(id=pk)
    form = DoctorUpdateForm(instance=doctor)
    if request.method == 'POST':
        doctor.first_name = request.POST.get('first_name')
        doctor.first_name = request.POST.get('first_name')
        doctor.email = request.POST.get('email')
        doctor.save()
        return redirect('doctors')
    
    context = {'form': form}
    return render(request, 'update_doctor.html',context)

def doctor_delete(request,pk):
    doctor = User.objects.get(id=pk)
    
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')        
    return render(request,'delete_doctor.html',{'doctor':doctor})

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
    assistant = Assistant.objects.get(id=pk)
    form = DoctorUpdateForm(instance=assistant)
    if request.method == 'POST':
        assistant.first_name = request.POST.get('first_name')
        assistant.first_name = request.POST.get('first_name')
        assistant.email = request.POST.get('email')
        assistant.save()
        return redirect('assistants')
    
    context = {'form': form}
    return render(request, 'update_assistant.html',context)

def assistant_delete(request,pk):
    assistant = Assistant.objects.get(id=pk)
    
    if request.method == 'POST':
        assistant.delete()
        return redirect('assistants')        
    return render(request,'delete_assistant.html',{'assistant':assistant})

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
    patient = Patient.objects.get(id=pk)
    form = DoctorUpdateForm(instance=patient)
    if request.method == 'POST':
        patient.first_name = request.POST.get('first_name')
        patient.first_name = request.POST.get('first_name')
        patient.email = request.POST.get('email')
        patient.save()
        return redirect('patients')
    
    context = {'form': form}
    return render(request, 'update_patient.html',context)

def patient_delete(request,pk):
    patient = Patient.objects.get(id=pk)
    
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')        
    return render(request,'delete_patient.html',{'patient':patient})

def treatment_register(request):
    form = TreatmentForm()

    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.save()
            
            return redirect('treatments')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'treatment_register.html', {'form': form})

def treatment_update(request, pk):
    treatment = Treatment.objects.get(id=pk)
    form = TreatmentUpdateForm(instance=treatment)
    if request.method == 'POST':
        treatment.name = request.POST.get('name')
        treatment.description = request.POST.get('description')
        treatment.patient = request.POST.get('patient')
        treatment.save()
        return redirect('treatments')
    
    context = {'form': form}
    return render(request, 'update_treatment.html',context)

def treatment_delete(request, pk):
    treatment = Treatment.objects.get(id=pk)
    
    if request.method == 'POST':
        treatment.delete()
        return redirect('treatments')        
    return render(request,'delete_treatment.html',{'treatment':treatment})