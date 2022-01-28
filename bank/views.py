# importing the necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from bank.models import BankModel
from .forms import AccountRequestForm
from django.contrib.auth.decorators import login_required


"""
name: Home View
desc: This view handles the homepage and the information that is to be
        displayed there.
"""
@login_required(login_url='login')
def HomeView(request):
    return render(request,'home.html',{})


"""
name: Register Request View
desc: Banks can request to create an account for them through this endpoint.
"""
def BankRegistrationRequestView(request):
    if request.method == "POST":
        form = AccountRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = AccountRequestForm()
    return render(request,'bank/register.html',{'form':form})


"""
name: Login View
desc: used by banks for authentication
"""
def BankLoginView(request):
    if request.method == "POST":
        bank = authenticate(request,email=request.POST['email'],password=request.POST['password'])
        if bank:
            login(request,bank)
            return redirect('home')
        else:
            print("email id not match with pass")
            messages.error(request,"Email Id and Password does not Match")
            return redirect('login')
    return render(request,'bank/login.html',{})


"""
name: Logout View
desc: Sign out of their account
"""
def LogoutView(request):
    logout(request)
    return redirect('login')


"""
name: Profile View
desc: Banks details are displayed here and can be updated.
"""
@login_required(login_url='login')
def BankProfileView(request):
    bank = request.user
    return render(request,'bank/profile.html',{'bank':bank})

"""
name: Profile Update View
desc: Banks details can be updated here.
"""
@login_required(login_url='login')
def BankProfileUpdateView(request):
    bank = request.user
    if request.method == "POST":
        BankModel.objects.filter(bankname=bank.bankname).update(
            bankname=request.POST['bankname'],
            email=request.POST['email'],
            address=request.POST['address'],
            contactnumber=request.POST['contactnumber']
        )
        return redirect('update')
    return render(request,'bank/update.html',{'bank':bank})

"""
name:Password Change View
desc: this endpoint is used to change the password of a bank account
"""
def PasswordChangeView(request):
    return render(request,'bank/passChange.html',{})