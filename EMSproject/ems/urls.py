from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
<<<<<<< HEAD
    path('dashboard',views.login),
    path('add_emp/',views.add_emp),
=======
    path('login',views.login),
    path('add_emp/',views.add_emp)
>>>>>>> 13a73185d6c85463dc26fbf5ffa99fc525580cae
]
