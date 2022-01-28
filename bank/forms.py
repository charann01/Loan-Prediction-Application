from django import forms
from .models import AccountRequestTable


class AccountRequestForm(forms.ModelForm):
    class Meta:
        model = AccountRequestTable
        fields = "__all__"


class passwordChangeForm(forms.Form):
    new_password = forms.CharField(min_length=6,widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    current_password = forms.CharField(min_length=6,widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('new_password')
        pass2 = cleaned_data.get('confirm_password')
        if pass1 != pass2:
            raise forms.ValidationError("Passwords fo not match")

    