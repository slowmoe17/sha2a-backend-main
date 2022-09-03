from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
import datetime
from django.core.cache import cache


from .managers import CustomUserManager
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=14)
    username = models.CharField(max_length=255, blank=True, null=True)


    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=200 , null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('phone', )

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ProfileImg(models.Model):
    user = models.OneToOneField('users.Profile', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_img', blank=True)
    def __str__(self):
        return self.img.url




class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , blank=True, null=True)
    type = (

        ("seeking", "seeking"),

        ("offering", "offering"),

    )
    country = models.CharField(max_length=100 , blank=True, null=True)
    city = models.CharField(max_length=100 , blank=True, null=True)
    profile_photo = models.ForeignKey(ProfileImg, on_delete=models.CASCADE, blank=True, null=True)
    profile_type = models.CharField(max_length=10, choices=type ,blank=True, null=True)




  