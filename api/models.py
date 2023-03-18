from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password

class RoleChoices(models.TextChoices):
    DOCTOR = 'doctor', 'Doctor'
    GENERAL_MANAGER = 'general_manager', 'General Manager'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    def __str__(self):
        return self.user.get_full_name()

class Assistant(User):
    patients = models.ManyToManyField('Patient', related_name='assistant_patients',blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Assistants"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Patient(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(unique=True)
    assistants = models.ManyToManyField(Assistant, related_name='patient_assistants',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Treatment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.name}"