from django.contrib import admin
from .models import UserProfile, Assistant, Patient, Treatment

admin.site.register(UserProfile)
admin.site.register(Assistant)
admin.site.register(Patient)
admin.site.register(Treatment)