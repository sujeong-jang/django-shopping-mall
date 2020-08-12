from .models import User
from .forms import SignUpForm, SignInForm

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth import authenticate

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
        form = SignInForm
        return render(request, 'users/signin.html', {'form':form})
    
    def post(self, request):
        form = SignInForm(request.POST)

        email = request.POST['email']
        password = request.POST['password']

        # authenticate를 통해 DB에 있는 email, password값과 사용자가 입력한 값 비교 
        user = authenticate(email=email, password=password)
        
        # 사용자가 입력한 값이 존재한다면
        if user:
            auth.login(request, user=user)
            return redirect('home')
        else:
            form.add_error('아이디 또는 비밀번호가 일치하지 않습니다.')
            return render(request, 'usets/signup.html', {'form':form})

class SignOutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')