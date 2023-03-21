from django.forms import ModelForm
from django import forms
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
    patients = forms.ModelMultipleChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class PatientForm(ModelForm):
    assistants = forms.ModelMultipleChoiceField(
        queryset=Assistant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Patient
        fields = '__all__'
        
class PatientUpdateForm(ModelForm):
    assistants = forms.ModelMultipleChoiceField(
        queryset=Assistant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
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