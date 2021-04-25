from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard',views.login),
    path('add_emp/',views.add_emp),
    path('logout',views.logout), 
    path('update/<empid>', views.update),
    path('delete/<empid>', views.destroy),    
]
