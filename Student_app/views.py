from django.shortcuts import render, HttpResponse
import mysql.connector as mcdb
from .models import Student

# Create your views here.

conn = mcdb.connect(host="localhost", user="root", password="", database='studentdb')
print('Successfully connected to database')
cur = conn.cursor()
# ------------------------------------------------------------------------
def home(request):
    # return HttpResponse("Home")
    return render(request,"home.html")

def add1(request):
    return render(request,"add.html")

def add(request):
    print("_______________________________________________1")
    if request.method == "POST":
        print("_______________________________________________2")
        fname = request.POST.get('name1')
        lname = request.POST.get('name2')
        age = request.POST.get('age')
        email = request.POST.get('email')
        cls1 = request.POST.get('cls')
        dt = request.POST.get('dt')

        p = Student(fname = fname, lname = lname, age= age, email = email, sclass = cls1, join_dt= dt)
        print("==================",fname, lname, age, email)
        p.save()
        # cur.exexcute()
        print("------------success------------------")
        # return render(request,"show.html")        
        
    print("------------fail------------------")  
    # return render(request, 'home.html')
