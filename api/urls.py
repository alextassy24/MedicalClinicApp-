from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('doctors/', views.view_doctors, name='doctors'),
    path('doctors/<str:pk>', views.view_doctor, name='doctors'),
    
    path('assistants/', views.view_assistants, name='assistants'),
    path('assistants/<str:pk>', views.view_assistant, name='assistants'),
    
    path('treatments/', views.view_treatments, name='treatments'),
    path('treatments/<str:pk>', views.view_treatment, name='treatments'),
    
    
    path('patients/', views.view_patients, name='patients'),
    path('patients/<str:pk>', views.view_patient, name='patients'),
    
]