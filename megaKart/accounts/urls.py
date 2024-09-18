from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),


    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),

    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('resetPassword/', resetPassword, name='resetPassword'),


]
