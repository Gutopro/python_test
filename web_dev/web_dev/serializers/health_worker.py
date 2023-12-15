from rest_framework import serializers
from ..models.health_worker import HealthWorker
from django.contrib.auth.hashers import make_password

class HealthWorkerSerializer(serializers.ModelSerializer):
    """ Serializer for Health Worker model """
    class Meta:
        model = HealthWorker
        fields = '__all__'

    def create(self, validated_data):
        """ Hashes a password before saving in the database """
        password = make_password(validated_data["password"])
        validated_data["password"] = password
        return HealthWorker.objects.create(**validated_data)

