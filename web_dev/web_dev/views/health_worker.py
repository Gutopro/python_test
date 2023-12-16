""" All related views to health worker """

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password

from ..models.health_worker import HealthWorker
from ..serializers.health_worker import HealthWorkerSerializer
from ..utils.jwt_utils import generate_token, get_user_from_request

@api_view(["POST"])
def health_worker_login(request):

    """ Health Worker login """

    email = request.data.get("email",None)
    password = request.data.get("password",None)
    user = None
    if not password or not email:
        return Response({"Message": "email and password are required to login"},
                        status = status.HTTP_400_BAD_REQUEST)
    try:
        user = HealthWorker.objects.get(email=email)
    except HealthWorker.DoesNotExist:
        pass
    if user and check_password(password, user.password) and user.is_active:
        token = generate_token(user)
        return Response({
            "message": "Successfull login",
            "token": token,
            })
    if user and check_password(password, user.password) and not user.is_active:
        return Response({
            "message": "account deactivated",
            }, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"Message": "Wrong Credentials"}, status=status.HTTP_401_UNATHORIZED)

@api_view(['GET', 'POST'])
def create_health_worker(request):
    """Get the list of health workers or create a new health workers"""
    if request.method == 'POST':
        serializer = HealthWorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "HealthWorker created successfully",
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
