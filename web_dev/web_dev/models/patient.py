from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from email_validator import validate_email, EmailNotValidError
from .base_model import BaseModel

def custom_email_validator(value):
        try:
                    validate_email(value)
        except EmailNotValidError as e:
                    raise ValidationError(str(e))


class Patient(BaseModel):
        """ Patient user definition"""
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        email = models.CharField(max_length=200, unique=True, validators=[custom_email_validator])
        phone_number = models.CharField(max_length=200, unique=True)
        password = models.CharField(max_length=200)
        is_active = models.BooleanField(default=True)
