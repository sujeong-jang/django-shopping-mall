from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def shop(request):
   products = Product.objects.all()
   context = {'products': products}
   return render(request, 'product/shop.html', context)

def outer(request):
    outer = Product.objects.filter(category='O')
    context = {'outer': outer}
    return render(request, 'product/outer.html', context)

def top(request):
    top = Product.objects.filter(category='T')
    context = {'top': top}
    return render(request, 'product/top.html', context)

def pants(request):
    pants = Product.objects.filter(category='P')
    context = {'pants': pants}
    return render(request, 'product/pants.html', context)

def skirt(request):
    skirt = Product.objects.filter(category='S')
    context = {'skirt': skirt}
    return render(request, 'product/skirt.html', context)