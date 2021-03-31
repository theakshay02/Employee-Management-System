from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'log.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            details=Employee.objects.filter(empid=username)
            table=Employee.objects.all()
            
            if  details[0].isadmin == False:
                return render(request,'dashboard.html',{'details':details})
            else:
                return render(request,'admin.html',{'details':details,'table':table})


        else:
            messages.info(request,'Invalid credentials are entered, please try again!')
            return redirect('/')
    else:
        return render(request,'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def add_emp(request):
    """ empid=request.POST['empid']
    name=request.POST['ename']
    role=request.POST['role']
    phno=request.POST['phno']
    email=request.POST['email']
    address=request.POST['address']
    img=request.POST['img']
    salary=request.POST['salary']
    leaves=request.POST['leaves'] """
    
    return render(request,'add_emp.html')