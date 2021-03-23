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
            print(details)
            
            if Employee.objects.values('isadmin') == 0:
                return render(request,'dashboard.html',{'details':details})
            else:
                return render(request,'admin.html',{'details':details})


        else:
            messages.info(request,'Invalid Credentials!!Please try again')
            return redirect('/')
    else:
        return render(request,'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
