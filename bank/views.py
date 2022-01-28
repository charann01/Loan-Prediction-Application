from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import AccountRequestForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomeView(request):
    return render(request,'home.html',{})

def BankRegistrationRequestView(request):
    if request.method == "POST":
        form = AccountRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = AccountRequestForm()
    return render(request,'bank/register.html',{'form':form})

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

def LogoutView(request):
    logout(request)
    return redirect('login')