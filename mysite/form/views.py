from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    first_name = request.POST.get('first_name')
    print(first_name)
    last_name = request.POST.get('last_name')
    print(last_name)
    email = request.POST.get('email')
    print(email)
    phone = request.POST.get('phone')
    print(phone)
    address = request.POST.get('address')
    print(address)
    additional_info = request.POST.get('additional_info')
    print(additional_info)
    company_name = request.POST.get('company_name')
    print(company_name)
    return render(request,"CW_Front_Q2.html",{'first_name':first_name ,'last_name':last_name ,'email':email ,
                                              'phone':phone , 'address':address, 'additional_info':additional_info,
                                              'company_name':company_name})