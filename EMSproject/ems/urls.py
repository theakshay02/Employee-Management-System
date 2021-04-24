from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard',views.login),
    path('add_emp/',views.add_emp),
    path('logout',views.logout),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),    
]
