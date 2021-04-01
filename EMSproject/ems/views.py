from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
        if request.user.is_authenticated:
            details=Employee.objects.filter(empid=request.user.username)
            table=Employee.objects.all()
            
            if  details[0].isadmin == False:
                return render(request,'dashboard.html',{'details':details})
            else:
                return render(request,'admin.html',{'details':details,'table':table})
        else:   
            return render(request,'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required()
def add_emp(request):
    if request.method == 'POST' and request.FILES['image']:
        empid=request.POST['empid']
        name=request.POST['ename']
        role=request.POST['role']
        isadmin=request.POST['admin']
        gender=request.POST['gender']
        phno=request.POST['phno']
        email=request.POST['email']
        address=request.POST['address']
        salary=request.POST['salary']
        leaves=request.POST['leaves']
        img=request.FILES['image']
        
        if User.objects.filter(username=empid).exists() == False:
            
            emp=Employee(empid=empid,name=name,role=role,phone=phno,email=email,
                        gender=gender,address=address,img=img,salary=salary,leaves=leaves,isadmin=isadmin)
            emp.save()
            
            user = User.objects.create_user(username=empid,password='root#123@')
            user.save()
            messages.info(request,'Employee added successfully :) ')
            return redirect('/add_emp')
        else:
            messages.info(request,'Employee already exist :) ')
            return redirect('/add_emp')

    else:
        return render(request,'add_emp.html')

     
        
     
   
