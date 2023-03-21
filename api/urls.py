from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    
    path('doctors/', views.view_doctors, name='doctors'),
    path('doctors/<str:pk>', views.view_doctor, name='doctors'),
    path('doctors-register/', views.doctor_register, name='doctors-register'),
    path('doctors-update/<str:pk>', views.doctor_update, name='doctors-update'),
    path('doctors-delete/<str:pk>', views.doctor_delete, name='doctors-delete'),
    
    path('assistants/', views.view_assistants, name='assistants'),
    path('assistants/<str:pk>', views.view_assistant, name='assistants'),
    path('assistants-register/', views.assistant_register, name='assistants-register'),
    path('assistants-update/<str:pk>', views.assistant_update, name='assistants-update'),
    path('assistants-delete/<str:pk>', views.assistant_delete, name='assistants-delete'),
    
    path('treatments/', views.view_treatments, name='treatments'),
    path('treatments-register/', views.treatment_register, name='treatments-register'),
    path('treatments/<str:pk>', views.view_treatment, name='treatments'),
    path('treatments-update/<str:pk>', views.treatment_update, name='treatments-update'),
    path('treatments-delete/<str:pk>', views.treatment_delete, name='treatments-delete'),
    
    
    path('patients/', views.view_patients, name='patients'),
    path('patients/<str:pk>', views.view_patient, name='patients'),
    path('patients-register/', views.patient_register, name='patients-register'),
    path('patients-update/<str:pk>', views.patient_update, name='patients-update'),
    path('patients-delete/<str:pk>', views.patient_delete, name='patients-delete'),
    
    
    
]