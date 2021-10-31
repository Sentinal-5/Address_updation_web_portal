from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class TenantForm(forms.Form):
    landlord_number = forms.CharField(max_length=12, validators=phone_regex)
    address = forms.CharField(max_length=200)
