from django import forms

choice = ['ADHAAR NUMBER', 'MOBILE NUMBER']


class LoginForm(forms.Form):
    inp = forms.IntegerField(
        max_value=12,
        label="user_input",
        widget=forms.Select(choices=choice))
