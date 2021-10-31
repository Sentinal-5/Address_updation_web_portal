from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid

# Create your models here.

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                     "allowed.")


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17, validators=[phone_regex], unique=True)
    address = models.CharField(max_length=200, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


class activeuser(models.Model):
    user = models.CharField(max_length=17, validators=[phone_regex], unique=True)
    phone_number = models.CharField(max_length=17, unique=True)
    address = models.CharField(max_length=200, unique=True)
