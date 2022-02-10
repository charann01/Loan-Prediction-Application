from django import forms
from .models import SheetModel

class SingleUserDetailForm(forms.Form):
    email = forms.EmailField()
    salary = forms.IntegerField(max_value=100000000)
    has_family = forms.CharField()
    send_mail = forms.BooleanField(label='Send mail to client ?')

class SheetForm(forms.ModelForm):
    class Meta:
        model = SheetModel
        fields = ('sheet',)