from django.shortcuts import render, HttpResponse
from .forms import SingleUserDetailForm, SheetForm
from .models import SheetModel
import os
import numpy as np
import pandas as pd


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

"""
name: Sheet Report
description: csv file is uploaded and the view returns the csv along with predictions
"""
def SheetReport(request):
    form = SheetForm()
    if request.method == "POST":
        form = SheetForm(request.POST,request.FILES)
        if form.is_valid():
            sheet = SheetModel(**form.cleaned_data,bank=request.user)
            sheet.save()
            
            data = pd.read_csv(sheet.sheet.path)
            new_col = np.random.randint(low=0,high=2,size=data.shape[0])
            data['target'] = new_col

            os.remove(sheet.sheet.path)
            sheet.delete()

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=export.csv'
            data.to_csv(path_or_buf=response)
            return response

    return render(request,'report/sheet.html',{'form':form})