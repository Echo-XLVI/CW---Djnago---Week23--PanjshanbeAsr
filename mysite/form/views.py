from django.shortcuts import render
from django.http import HttpResponse
from mysite.databaseconnection import DataBaseConnection
# import psycopg2

# Create your views here.
def home_page(request):

    db_manager = DataBaseConnection()
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        additional_info = request.POST.get('additional_info')
        company_name = request.POST.get('company_name')
        print(first_name)
        query = "insert into users (firstname ,lastname ,company ,email ,phone ,address ,about ) values (%s,%s,%s,%s,%s,%s,%s)"
        params = (first_name , last_name , email , phone , address,additional_info,company_name)
        with db_manager as db :
            db.cursor.execute(query,params)

        return HttpResponse("<h1>succeded</h1>")


  
    return render(request,"CW_Front_Q2.html")