from rest_framework import viewsets

from ..models.medic_info import MedicalInformation
from ..serializers.medic_info import MedicalInformationSerializer

class MedicalInformationViewSet(viewsets.ModelViewSet):
    queryset = MedicalInformation.objects.all()
    serializer_class = MedicalInformationSerializer
