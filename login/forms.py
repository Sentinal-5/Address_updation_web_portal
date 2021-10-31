from django import forms
from .models import Users, phone_regex


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=17, validators=[phone_regex])

    class Meta:
        model = Users
        fields = ['phone_number']
