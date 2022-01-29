from django.db import models
from bank.models import BankModel

# Create your models here.
class SheetModel(models.Model):
    sheet = models.FileField(upload_to='sheets/')
    bank = models.OneToOneField(BankModel,on_delete=models.CASCADE)
