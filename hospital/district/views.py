from django.shortcuts import redirect, render
from django.http import HttpResponse
from division.models import Divisions
from .models import Districts
# Create your views here.


def index(request):
    data = Divisions.objects.all().order_by('divisionname')
    data2 = Districts.objects.select_related('div_id').all()
    data_context = {'d':data,'d2':data2}
    return render(request,'admin/district.html',data_context)


def district_insert(request):
    id = request.POST.get('id')
    name = request.POST.get('name')

    dis_obj = Districts()

    div_obj = Divisions.objects.get(id=id)

    dis_obj.districtname = name
    dis_obj.div_id = div_obj
    dis_obj.save()

    return redirect('dis_index')

