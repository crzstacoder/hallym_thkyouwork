
from django import forms

class signup(forms.Form) :
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm_Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password == None or confirm_password == None :
            raise forms.ValidationError("Password and confirm_password cannot be empty")
        elif password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")