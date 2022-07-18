import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserModel(models.Model):
    email = models.EmailField(
        verbose_name="email",
        unique=True
    )
    username = models.CharField(
        verbose_name="Họ và tên",
        max_length=255
    )
    phone_regex = RegexValidator(
        regex=r'^\+?2?\d{8,14}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )

    objects = CustomUserManager()

    

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perm(self, app_label):
        return True


UserModel = get_user_model()
class Product(models.Model):
    """"""
