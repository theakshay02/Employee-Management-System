from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    address=models.TextField()
    img=models.ImageField(upload_to='pics',default='None',null=True)
    salary=models.IntegerField(default=0,null=True)
    leaves=models.IntegerField(default=0,null=True)
    isadmin=models.BooleanField(default=False,null=True)