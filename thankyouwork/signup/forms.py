
from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form) :
    username = forms.CharField(label='Username', max_length=10)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm_Password', widget=forms.PasswordInput)

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get(('password'))

        user = User.objects.create_user(username=username, email=email, password = password)
        return user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password == None or confirm_password == None :
            raise forms.ValidationError("Password and confirm_password cannot be empty")
        elif password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")