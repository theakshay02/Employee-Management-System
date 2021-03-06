from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index),
    path('dashboard',views.login),
    path('add_emp/',views.add_emp),
    path('logout',views.logout), 
    path('update/<empid>', views.update),
    path('delete/<empid>', views.destroy),
    path('update2/<empid>', views.update2),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), 
     name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), 
     name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
   
    path('applyleave/<empid>',views.apply_leave),
    path('approveleave/<mgrid>/',views.approveleave),
    path('leavehistory/<empid>',views.leavehistory),
    path('approve/<empid>',views.approve),
    path('decline/<empid>',views.decline),
]
