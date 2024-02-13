from django.shortcuts import redirect, render
from django.http import HttpResponse
from division.models import Divisions
from district.models import Districts
# Create your views here.
from django.db.models import Count
from .models import Station

def index(request):
    # data = Divisions.objects.all().order_by('divisionname')
    data2 = Districts.objects.values_list('div_id__divisionname', 'div_id__id', flat=False).distinct()
    # data3 = Districts.objects.values_list('Districtname', flat=True).distinct()
    
    data3 = Districts.objects.all()

    data_context = {'d2':data2,'d3':data3}
    return render(request,'admin/station.html',data_context)


def district_insert(request):
    div_id = request.POST.get('div_id')
    dis_id = request.POST.get('dis_id')
    name = request.POST.get('name')

    st_obj = Station()

    div_obj = Divisions.objects.get(id=div_id)
    dis_obj = Districts.objects.get(id=dis_id)

    st_obj.name = name
    st_obj.div_id = div_obj
    st_obj.dis_id = dis_obj
    st_obj.save()

    return redirect('station_index')
from django.shortcuts import render
# Create your views here.


