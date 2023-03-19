from django.forms import ModelForm
from .models import Assistant, Patient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        
class AssistantForm(UserCreationForm):
    class Meta:
        model = Assistant
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__' 