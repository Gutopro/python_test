from django.db import models
from .base_model import BaseModel
from .patient import Patient

class MedicalInformation(BaseModel):

    choices = (('Yes', 'Yes'), ('No', 'No'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Allergies = models.CharField(max_length=200, default='Do you have any allergies?', choices=choices)
    Surgery = models.CharField(max_length=200, default='Have you ever had surgery?', choices=choices)
    On_Medications = models.CharField(max_length=200, default='Are you currently taking any medication?', choices=choices)
    Heart_Disease_History = models.CharField(max_length=200, default='Do you have history of heart disease in your family?', choices=choices)
    History_of_Diabetes = models.CharField(max_length=200, default='Do you have a history of Diabetes in your family?', choices=choices)
