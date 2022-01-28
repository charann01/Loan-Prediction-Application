from django.urls import path
from .views import BankLoginView, BankRegistrationRequestView, LogoutView

urlpatterns = [
    path('',BankRegistrationRequestView,name='register'),
    path('login/',BankLoginView, name='login'),
    path('logout/',LogoutView,name='logout')
]