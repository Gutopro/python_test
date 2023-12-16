from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.health_worker import HealthWorker
from ..models.patient import Patient
from ..serializers.patient import PatientSerializer
from ..utils.jwt_utils import generate_token, get_user_from_request

@api_view(['POST', 'GET'])
def create_patient(request):
    """Get the list of patients or create a new patient"""
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Patient created successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response = {
            'message':'Something went wrong',
            'error': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        user = get_user_from_request(request)
        # If token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def patient_login(request):
        '''This view handles patient login'''
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = None
        if not password or not email:
            return Response({
                "message": "email and password are required to login"
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Patient.objects.get(email__iexact=email.lower())
        except Patient.DoesNotExist:
            pass
        if user and check_password(password, user.password) and user.is_active:
            token = generate_token(user)
            return Response({
                "message": "Login successful",
                "token": token
            }, status=status.HTTP_200_OK)
        if user and user.password and not user.is_active:
            return Response({
                "message": "account deactivated"
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            "message": "Wrong credentials"
        }, status=status.HTTP_401_UNAUTHORIZED)
