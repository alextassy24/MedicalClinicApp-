from django.forms import ModelForm
from .models import Assistant, Patient, Treatment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        
class DoctorUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class AssistantForm(UserCreationForm):
    class Meta:
        model = Assistant
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        
class AssistantUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__' 
        
class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__' 
        
class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__' 
        
class TreatmentUpdateForm(ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__' 