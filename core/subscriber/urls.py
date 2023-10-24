from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', views.user_login, name='login'),
    path('register/', views.user_registration, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('profile/', views.users_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    
    # passwor-reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='subscriber/password_reset.html'), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='subscriber/password_reset_sent.html'), name='password_reset_done'),
    path('password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='subscriber/password_reset_done.html'), name='password_reset_complete'),
   

    # Pre-module-options-router
    path('pre_options/', views.user_options_pre, name='pre_options'),
    path('para_options/', views.user_options_para, name='para_options'),
    path('clinical_options/', views.user_options_clicnical, name='clinical_options'),

]

'''
Submit email form                            //PasswordResetView.as_view()
Email sent sucess message                    //PasswordResetDoneView.as_view()
Link to password Reset form in email         //PasswordResetConfirm.as_view()
Password sucessfull changed message          //PasswordResetComplete.as_view()

'''