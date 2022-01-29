from django.shortcuts import render
from .forms import SingleUserDetailForm

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
