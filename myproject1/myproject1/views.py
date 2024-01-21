from django.http import HttpResponse
from django.shortcuts import render,redirect

from . models import About
from django.contrib import messages

# import bleach
import random
import re
from django.core.signing import Signer
from django.core.mail import send_mail
from datetime import datetime
from django.utils.html import format_html

def demo(request):
    title = "this is a demo html"
    name = "lona"
    product_name = ['p1','p2','p3']
    data = {"t":title,'name':name,'prod':product_name}
    # print("this is a root url function ")
    return render(request,'demo/portfolio.html',data)

def about_index(request):  

    all_data = About.objects.all()
    msg = messages.get_messages(request)
    # print(msg)
    data = {'d': all_data,'msg':msg}  
    # print("this is a root url function ")
    return render(request,'admin/about.html',data)




def email_verify(request,id):
    data = About.objects.get(v_c=id)
    data.v_status = 1
    data.save()
    return redirect('about')

    # return HttpResponse(id)
def about_insert(request):
    name = request.POST.get('uname')
    dob = request.POST.get('dob') 
    phone = request.POST.get('phone') 
    email = request.POST.get('email') 
    exp = request.POST.get('exp') 
    no_cust = request.POST.get('no_cust')
    no_project = request.POST.get('no_project') 
    no_of_awards = request.POST.get('no_of_awards') 
    desc = request.POST.get('desc') 
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y - %I:%M %p")  
    pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$" 

    #  check if any of the required fields is empty
    # if not all([name, dob, phone, email, exp, no_cust, no_project, no_of_awards, desc]):
    #     # messages.clear()
        # messages.success(request,"The field can not be empty")
    #     # return HttpResponse("Error: All fields are required.")
    # else:
    # if not re.match(pattern, email):
    #     messages.success(request,"your email is not gmail")
    # elif len(phone)!=11:
    #     messages.success(request,"your mobile number must have 11 digits")
    # else: 

    #     data = About.objects.all()
    #     len_data = len(data)
    #     if (len_data >= 1):
    #         messages.success(request,"you can not entry more than one data")
    #     else:
    current_time = datetime.now().strftime("%H:%M:%S")
    # print(current_time)
    print(current_time.split(':'))
    h, m, s = map(int, current_time.split(':'))
    t_s = h*3600 + m*60 + s
    random_number = random.choices('1234567890',k=4)
    random_number = ''.join(random_number)
    t_s = str(t_s)
    v_c = t_s + random_number
    signer = Signer()
    encrypted_value = signer.sign(v_c).split(":")[1]
    
    link = f"<p>Congratulations Mr {name} ! For registering as a user in our myproject1 system. To confirm the registration </p><a href= 'http://127.0.0.1:8000/admin/user/email_verification/"+encrypted_value+"' target='_blank'>please click this Activation link</a>"
    send_mail(f"Mr. {name} please confirm your Registration - myproject1 panel",encrypted_value,'nowshadjl1979@gmail.com',[email],html_message=link)
                           
    # print(t_s,random_number)
    # print(v_c)
    print(encrypted_value)



    about_obj = About()

    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = exp
    about_obj.no_happy_customers = no_cust
    about_obj.no_project_finished = no_project
    about_obj.no_digital_awards = no_of_awards
    about_obj.description = desc
    about_obj.date_time = formatted_datetime
    about_obj.v_c = encrypted_value
    about_obj.v_status = 0
    about_obj.save()


    # print("this is a root url function ")
    return redirect('about')

def edit_index(request,id):

    data = About.objects.get(id=id)
    d = {'data':data}
    return render(request,'admin/edit.html',d)


def about_edit(request):

    id = request.POST.get('id')
    name = request.POST.get('uname')
    dob = request.POST.get('dob') 
    phone = request.POST.get('phone') 
    email = request.POST.get('email') 
    exp = request.POST.get('exp') 
    no_cust = request.POST.get('no_cust')
    no_project = request.POST.get('no_project') 
    no_of_awards = request.POST.get('no_of_awards') 
    desc = request.POST.get('desc') 
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d %b %Y - %I:%M %p") 
    # pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$" 

    
    about_obj = About.objects.get(id=id)

    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = exp
    about_obj.no_happy_customers = no_cust
    about_obj.no_project_finished = no_project
    about_obj.no_digital_awards = no_of_awards
    about_obj.description = desc
    about_obj.date_time = formatted_datetime

    about_obj.save()


    # print("this is a root url function ")
    return redirect('about')

def delete_index(request,id):

    data = About.objects.get(id=id)
    data.delete()
    return redirect('about')


