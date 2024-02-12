from django.shortcuts import redirect, render
from django.http import HttpResponse
from division.models import Divisions
from .models import Districts
# Create your views here.


def index(request):
    data = Divisions.objects.all()
    data_context = {'d':data}
    return render(request,'admin/district.html',data_context)

def district_insert(request):
    idddd = request.POST.get('id')
    nammmm = request.POST.get('name')
    div_idddd = Divisions.objects.get(id=idddd)

    dist = Districts()
    
    dist.Districtname = nammmm
    dist.div_id = div_idddd
    dist.save()

    return redirect('dis_index')
