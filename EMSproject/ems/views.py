from django.shortcuts import render,redirect
import os
from .models import Employee,EmpMgrDept,Applyforleave,Approveleave
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
                authr=['Manager','HR','Senior Manager']
                return render(request,'dashboard.html',{'details':details,'group':authr})
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
                authr=['Manager','HR','Senior Manager']
                return render(request,'dashboard.html',{'details':details,'group':authr})
            else:
                return render(request,'admin.html',{'details':details,'table':table})
        else:   
            return redirect('/')

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
            
            user = User.objects.create_user(username=empid,password='root#123@',email=email)
            user.save()
            messages.info(request,'Employee added successfully :) ')
            return redirect('/add_emp')
        else:
            messages.info(request,'Employee already exist :) ')
            return redirect('/add_emp')

    else:
        return render(request,'add_emp.html')



def update(request, empid):  
    if request.method == 'POST':
        
        employee = Employee.objects.get(empid=empid)   
        
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

    
        messages.info(request,'Employee Updated Successfully ')
        return render(request, 'edit.html', {'employee': employee})
        
    else:
        employee = Employee.objects.get(empid=empid)  
        return render(request,'edit.html', {'employee':employee})

def update2(request, empid):  
    if request.method == 'POST':
        
        employee = Employee.objects.get(empid=empid)   
        phno=request.POST['phno']
        email=request.POST['email']
        address=request.POST['address']

        emp = Employee.objects.get(empid=empid)           
        Employee.objects.filter(empid=empid).update(phone=phno,email=email,
                            address=address)   
        employee.refresh_from_db()
        messages.info(request,'Your information is updated successfully. ')
        return render(request, 'edit2.html', {'employee': employee})
        
    else:
        employee = Employee.objects.get(empid=empid)  
        return render(request,'edit2.html', {'employee':employee})

def destroy(request, empid):  
    employee = Employee.objects.get(empid=empid)  
    employee.delete()  
    return redirect("/dashboard")  

def apply_leave(request,empid):
    if request.method == 'POST':
        leave=request.POST['options']
        bdate=request.POST['BeginDate']
        edate=request.POST['Enddate']
        avail=request.POST['adays']
        req=request.POST['rdays']
        reason=request.POST['reason']

        leave_req=Applyforleave(emp_id=empid,leave_type=leave,begin_date=bdate,
        end_date=edate,avial_days=avail,req_days=req,reason=reason,status='Pending')

        leave_req.save()
        empl=EmpMgrDept.objects.get(Emp_No=empid)
        app_leave=Approveleave(emp_id=empid,emp_name=empl.Emp_Name,leave_type=leave,begin_date=bdate,end_date=edate,avial_days=avail,
        req_days=req,reason=reason,status='Pending',Mgr_id=empl.Manager_Emp_ID.empid
        )
        app_leave.save()
        
        return render(request,'leave/ApplyForLeave.html')
    else:
        emp = Employee.objects.get(empid=empid)
        return render(request,'leave/ApplyForLeave.html',{'emp':emp})


def approveleave(request,mgrid):
    requests=Approveleave.objects.all().filter(Mgr_id=mgrid)
    return render(request,'leave/ApproveLeave.html',{'requests':requests})

def leavehistory(request,empid):
    requests=Applyforleave.objects.all().filter(emp_id=empid)
    return render(request,'leave/LeaveHistory.html',{'requests':requests})

def approve(request,empid):
    Applyforleave.objects.filter(emp_id=empid).update(status='Approved')
    Approveleave.objects.filter(emp_id=empid).update(status='Approved')
    empl=EmpMgrDept.objects.get(Emp_No=empid)
    requests=Approveleave.objects.all().filter(Mgr_id=empl.Manager_Emp_ID.empid)
    return render(request,'leave/ApproveLeave.html',{'requests':requests})
    



def decline(request,empid):
    Applyforleave.objects.filter(emp_id=empid).update(status='Declined')
    Approveleave.objects.filter(emp_id=empid).update(status='Declined')
    empl=EmpMgrDept.objects.get(Emp_No=empid)
    requests=Approveleave.objects.all().filter(Mgr_id=empl.Manager_Emp_ID.empid)
    return render(request,'leave/ApproveLeave.html',{'requests':requests})
    


   
