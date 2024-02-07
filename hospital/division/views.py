from django.shortcuts import render,HttpResponse,redirect


# Create your views here.
from .models import Divisions


def index(request): 
    return render(request,'admin/division.html')


def insert(request): 
   name = request.POST.get('name')
   div = Divisions()
   div.name= name
   div.save()
   return redirect('index')