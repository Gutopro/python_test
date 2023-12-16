from rest_framework import serializers
from ..models.medic_info import MedicalInformation

class MedicalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInformation
        fields = '__all__'
