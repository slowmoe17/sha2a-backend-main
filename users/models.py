from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    type = (
        ('driver', 'Driver'),
        ('hotel', 'Hotel'),
        ('customer', 'Customer'),
    )
 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    username = models.CharField(max_length=255, unique=True)
    hotel_name = models.CharField(max_length=255,blank=True, null=True)
    user_type = models.CharField(max_length=255, choices=type, default='customer')



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']


    objects = CustomUserManager()

    def DriverFilter(self):
        if self.user_type == 'driver':
            hotel_name = "Null"
        return self.objects.filter(user_type='driver')

        





    def __str__(self):
        return self.username


class Driver(models.Model):
    full_name = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name



class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    








