from django.contrib import admin
from .models import BankModel, AccountRequestTable

# Register your models here.
admin.site.register(BankModel)
admin.site.register(AccountRequestTable)