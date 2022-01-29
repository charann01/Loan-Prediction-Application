from django.shortcuts import render
from .forms import SingleUserDetailForm, SheetForm
from .models import SheetModel
import os

# Create your views here.
"""
name: Single user report
desc: banks can put in the data of the users and get their score for loan prediction
"""
def SingleUserReport(request):
    form = SingleUserDetailForm()
    out = None
    if request.method == "POST":
        form = SingleUserDetailForm(request.POST)
        if form.is_valid():
            out = form.cleaned_data['salary'] > 30000
    return render(request,'report/single_user.html',{'form':form, 'out':out})

def SheetReport(request):
    form = SheetForm()
    if request.method == "POST":
        form = SheetForm(request.POST,request.FILES)
        if form.is_valid():
            sheet = SheetModel(**form.cleaned_data,bank=request.user)
            sheet.save()
            # do the necessary operations
            os.remove(sheet.sheet.path)
            sheet.delete()
    return render(request,'report/sheet.html',{'form':form})