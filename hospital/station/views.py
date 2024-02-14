from django.shortcuts import redirect, render
from django.http import HttpResponse
from division.models import Divisions
from district.models import Districts
# Create your views here.
from django.db.models import Count
from .models import Station

# from .forms import UploadFileForm

def index(request):
    # data = Divisions.objects.all().order_by('divisionname')
    data2 = Districts.objects.values_list('div_id__divisionname', 'div_id__id', flat=False).distinct()
    # data3 = Districts.objects.values_list('Districtname', flat=True).distinct()
    
    data3 = Districts.objects.all()
    data4 = Station.objects.select_related('div_id','dis_id').all()

    data_context = {'d2':data2,'d3':data3,'d4':data4}
    return render(request,'admin/station.html',data_context)

# import pandas as pd

# def csv_upload(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
            
#             df = pd.read_csv(file)
            
#             for index, row in df.iterrows():
                
#                 station_instance = Station()
                
#                 div_id=row['division']
#                 dis_id=row['district']
#                 div_obj = Divisions.objects.get(id=div_id)
#                 dis_obj = Districts.objects.get(id=dis_id)            

#                 station_instance.div_id = div_obj
#                 station_instance.dis_id = dis_obj
#                 station_instance.name = row['thana']
                
#                 station_instance.save()
#             return redirect('station_index')  # Redirect to a success page after data insertion
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

def district_insert(request):
    div_id = request.POST.get('div_id')
    dis_id = request.POST.get('dis_id')
    name = request.POST.get('name')
    image = request.FILES.get('image')

    st_obj = Station()

    div_obj = Divisions.objects.get(id=div_id)
    dis_obj = Districts.objects.get(id=dis_id)

    st_obj.name = name
    st_obj.div_id = div_obj
    st_obj.dis_id = dis_obj
    st_obj.image = image
    st_obj.save()

    return redirect('station_index')
from django.shortcuts import render
# Create your views here.


