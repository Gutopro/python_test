"""
URL configuration for web_dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views.health_worker import health_worker_login, create_health_worker
from .views.patient import create_patient
from .views.patient import patient_login
from .views.medic_info import MedicalInformationViewSet

urlpatterns = [
    path('health_workers/sign_up', create_health_worker),
    path('health_workers/login', health_worker_login),
    path('patients/sign_up', create_patient),
    path('patients/login', patient_login),
    path('patients/medic_info', MedicalInformationViewSet.as_view({'get': 'list', 'post': 'create'})),
    
]
