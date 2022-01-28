from django import forms
from .models import AccountRequestTable


class AccountRequestForm(forms.ModelForm):
    class Meta:
        model = AccountRequestTable
        fields = "__all__"