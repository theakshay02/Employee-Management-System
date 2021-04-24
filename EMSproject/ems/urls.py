from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard',views.login),
    path('add_emp/',views.add_emp),
    path('logout',views.logout),
    path('edit/<empid>', views.edit),  
    path('update/<empid>', views.update),    
]
