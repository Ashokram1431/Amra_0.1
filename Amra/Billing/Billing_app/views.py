from django.shortcuts import render
from . models import Medicine
# Create your views here.

def home(request):
    return render(request,'Home.html')

def product(request):
    context ={}
    context["medicine"] = Medicine.objects.all()
    return render(request,'Product.html',context)

def sales(request):
    context ={}
    context["medicine"] = Medicine.objects.all()
    return render(request,'Sales.html',context)

def addtocart(request):
    return render(request,'AddToCart.html')
