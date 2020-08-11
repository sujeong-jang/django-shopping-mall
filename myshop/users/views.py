from myshop.settings import SECRET_KEY
from .models import User
from .forms import SignUpForm

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView

from django.contrib import auth

class SignUpView(View):
    def get(self, request):
        form = SignUpForm
        return render(request, 'users/signup.html', {'form' : form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin')

        return render(request, 'users/signup.html', {'form': form})

class SignInView(View):
    def get(self, request):
        return render(request, 'users/signin.html')


class Logout(View):
    def post(self, request):
        auth.logout(request)
        return render(request, 'home')