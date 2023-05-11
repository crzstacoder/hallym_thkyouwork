from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

from .forms import signup

class SignUpView(View):
    def get(self, request):
        form = signup()
        return render(request, 'signup/signup.html', {'form': form})

    def post(self, request):
        form = signup(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
            return redirect('core:home')
        return render(request, 'signup/signup.html', {'form': form})