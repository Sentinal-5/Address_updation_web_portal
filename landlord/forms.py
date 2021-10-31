from django import forms


class LandlordForm(forms.Form):
    otp = forms.IntegerField(label="OTP")
