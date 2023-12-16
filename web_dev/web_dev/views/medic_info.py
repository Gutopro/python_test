from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models.medic_info import MedicalInformation
from ..serializers.medic_info import MedicalInformationSerializer
from ..models.patient import Patient
from ..serializers.patient import PatientSerializer

@api_view(['POST', 'GET'])
def create_medic_info(request):

    if request.method == 'POST':
        serializer = MedicalInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'medical information uploaded successfully',
                'data': serializer.data
                }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='GET':
        try:
            queryset = MedicalInformation.objects.all()
            height = request.query_params.get('height', None)
            weight = request.query_params.get('weight', None)
            id = request.query_params.get('id', None)

            if height:
                queryset = queryset.filter(height__icontains=height)
            if weight:
                queryset = queryset.filter(weight__icontains=weight)
            if id:
                queryset = queryset.filter(id__icontains=id)

            if not queryset:
                return Response({
                    'message': 'No data found'
                    }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(f'An error occurred: {e}')
            return Response({
                'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
