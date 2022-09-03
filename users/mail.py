import django
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import random

from users.models import CustomUser

def send_confirmation_email(user):
    subject = 'Confirm your registration to Sakeny '
    OTP = random.randint(100000, 999999)
    message = f'Hello {user.username}, you have been successfully registered to sakeny ,Your Confirmation OTP is : {OTP}'
    from_email = django.conf.settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
    user.otp = OTP
    user.save()
    return OTP


def send_welcome_email(user):
    subject = 'Welcome to Sakeny'
    message = f'Welcome {user.username} To sakeny , your account has been successfully activated'
    from_email = django.conf.settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
    return True




    
