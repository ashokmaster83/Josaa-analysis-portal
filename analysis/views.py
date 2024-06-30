from django.shortcuts import render
from .models import Data
import os

def josaa(request):
    data = Data.objects.all()
    return render(request,'analysis/josaa.html',{'data' : data})

#branches =[]
#directory_name = "branch/templates/branch"
#for file in os.listdir(directory_name):
 #       if file.endswith('.html'):
  #          branches.append(file)
 

def Institute_neutral(request):
    #data = Data.objects.all()
   # data = {'branches': branches}
    return render(request,'analysis/Institute_neutral.html')

def Institute_female(request):
    #data = Data.objects.all()
    return render(request,'analysis/Institute_female.html')

def Branch_neutral(request):
    #data = Data.objects.all()
    return render(request,'analysis/Branch_neutral.html')

def Branch_female(request):
    #data = Data.objects.all()
    return render(request,'analysis/Branch_female.html')







             

# Create your views here.
