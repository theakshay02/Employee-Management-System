from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    address=models.TextField()
    gender=models.CharField(max_length=15,default=None,null=True)
    img=models.ImageField(upload_to='pics',default='None',null=True)
    salary=models.IntegerField(default=0,null=True)
    leaves=models.IntegerField(default=0,null=True)
    isadmin=models.BooleanField(default=False,null=True)

class EmpMgrDept(models.Model):
    ID = models.AutoField(default=0,primary_key=True)
    Emp_No = models.CharField(max_length=20)
    Dept_ID = models.PositiveIntegerField(default=0)
    Manager_Emp_ID = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='Manager_Emp_ID',default=0)
    Emp_Name = models.CharField(max_length=50)
    Dept_Name = models.CharField(max_length=30)
    Manager_Name = models.CharField(max_length=50)
    Manager_Email = models.EmailField(max_length=70)

class Applyforleave(models.Model):
    emp_id=models.CharField(max_length=20)
    leave_type=models.CharField(max_length=30)
    begin_date=models.DateField()
    end_date=models.DateField()
    avial_days=models.IntegerField(default=0,null=True)
    req_days=models.IntegerField(default=0,null=True)
    reason=models.TextField()
    status=models.CharField(max_length=30)

class Approveleave(models.Model):
    emp_id=models.CharField(max_length=20)
    leave_type=models.CharField(max_length=30)
    begin_date=models.DateField()
    end_date=models.DateField()
    avial_days=models.IntegerField(default=0,null=True)
    req_days=models.IntegerField(default=0,null=True)
    reason=models.TextField()
    status=models.CharField(max_length=30)
    Mgr_id=models.ForeignKey(EmpMgrDept, on_delete=models.CASCADE,related_name='Mgr_id',default=0)