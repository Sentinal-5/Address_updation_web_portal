from django import forms
from django.core.validators import RegexValidator



class TenantForm(forms.Form):
    landlord_number = forms.CharField(max_length=12, )
