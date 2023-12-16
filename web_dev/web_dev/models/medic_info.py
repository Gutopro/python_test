from django.db import models
from .base_model import BaseModel
from .patient import Patient

class MedicalInformation(BaseModel):
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medic_info')
