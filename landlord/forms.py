from django import forms


class LandlordForm(forms.Form):
    otp = forms.IntegerField(max_value=4,label="OTP")
    tenant_name = forms.CharField()
    give_access = forms.CharField()
    deny_access = forms.CharField()
