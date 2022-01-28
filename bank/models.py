from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class AccountRequestTable(models.Model):
    bankName = models.CharField(max_length=128)
    email = models.EmailField(max_length=300)
    contactNumber = models.CharField(max_length=10)
    document = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.bankName

class BankManager(BaseUserManager):

    def create_user(self,email,bankname,contactnumber,password,**other_fields):
        if not email:
            raise ValueError("Email Id Required.")
        if not bankname:
            raise ValueError("Bank Name is Required.")
        if not contactnumber:
            raise ValueError("Contact Number is Required.")
        bank = self.model(email=self.normalize_email(email),bankname=bankname,contactnumber=contactnumber,**other_fields)
        bank.set_password(password)
        bank.save()
        return bank

    def create_superuser(self,email,bankname,contactnumber,password,**other_fields):
        other_fields.setdefault("is_active",True)
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_superuser",True)
        bank = self.create_user(email,bankname,contactnumber,password,**other_fields)
        bank.save()
        return bank


class BankModel(AbstractBaseUser, PermissionsMixin):
    bankname = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    contactnumber = models.CharField(max_length=10,unique=True)
    address = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['bankname','contactnumber','address']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = BankManager()

    def __str__(self):
        return self.email