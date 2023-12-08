from django.http import HttpResponse
from django.shortcuts import render



def demo(request):
    title = "this is a demo html"
    name = "lona"
    product_name = ['p1','p2','p3']
    data = {"t":title,'name':name,'prod':product_name}
    # print("this is a root url function ")
    return render(request,'demo/portfolio.html',data)