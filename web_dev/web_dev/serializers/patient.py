from rest_framework import serializers
from ..models.patient import Patient
from django.contrib.auth.hashers import make_password

class PatientSerializer(serializers.ModelSerializer):
        """Serializer for Patient model"""
        class Meta:
            model = Patient
            fields = '__all__'

        def create(self, validated_data):
           """ Hashes a password before saving in the database """
           password = make_password(validated_data["password"])
           validated_data["password"] = password
           return Patient.objects.create(**validated_data)
