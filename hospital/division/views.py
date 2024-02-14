from django.shortcuts import render,HttpResponse,redirect


# Create your views here.
from .models import Divisions


def index(request):
    alldivisions = Divisions.objects.all()
    context = {'d': alldivisions}
    return render(request,'admin/division.html', context)


def insert(request): 
   name = request.POST.get('name')

   div = Divisions()

   div.divisionname= name
   div.save()
   return redirect('index')

def search(request): 
   search_value = request.POST.get('search')
   search_result = Divisions.objects.filter(divisionname__icontains=search_value)
   print(len(search_result))
   return HttpResponse(len(search_result))

   