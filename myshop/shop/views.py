from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return render(request, 'shop/index.html')

def cart(request):
   return render(request, 'shop/cart.html')   

def checkout(request):
   return render(request, 'shop/checkout.html')

def board(request):
   return render(request, 'shop/board.html')