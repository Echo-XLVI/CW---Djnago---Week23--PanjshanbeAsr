from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    first_name = request.POST.get('first_name')
    print(first_name)
    return render(request,"CW_Front_Q2.html",{'first_name':first_name})