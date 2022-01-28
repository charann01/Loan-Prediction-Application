from django.urls import path
from .views import BankLoginView, BankRegistrationRequestView, LogoutView, BankProfileView, BankProfileUpdateView, PasswordChangeView

urlpatterns = [
    path('',BankRegistrationRequestView,name='register'),
    path('login/',BankLoginView, name='login'),
    path('logout/',LogoutView,name='logout'),
    path('profile/',BankProfileView,name='profile'),
    path('update/',BankProfileUpdateView,name='update'),
    path('password-change/',PasswordChangeView,name='passchange')
]