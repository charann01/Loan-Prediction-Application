from django import forms

class SingleUserDetailForm(forms.Form):
    email = forms.EmailField()
    salary = forms.IntegerField(max_value=100000000)
    has_family = forms.CharField()
    send_mail = forms.BooleanField(label='Send mail to client ?')
