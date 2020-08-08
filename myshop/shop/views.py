from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return render(request, 'shop/index.html')

def outer(request):
   return render(request, 'shop/outer.html')

def top(request):
   return render(request, 'shop/top.html')

def skirt(request):
   return render(request, 'shop/skirt.html')

def pants(request):
   return render(request, 'shop/pants.html')

def cart(request):
   return render(request, 'shop/cart.html')   

def checkout(request):
   return render(request, 'shop/checkout.html')