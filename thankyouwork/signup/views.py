from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import SignUpForm

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
            return redirect('signup:signuppage')
        return render(request, 'signup.html', {'form': form})

signup = SignUpView.as_view()