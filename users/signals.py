from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Profile
from django.db.models import signals
from users.models import CustomUser
from users.mail import send_confirmation_email , send_welcome_email

"""
this signal is used to create a profile for a new registered user
"""

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except CustomUser.DoesNotExist:
        pass
    else:
        instance.user.delete()
signals.post_delete.connect(delete_user, sender=Profile)


from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from users.mail import send_confirmation_email , send_welcome_email




@receiver(post_save, sender=CustomUser)
def send_verification_mail_to_user(sender, instance, created, **kwargs):
    if created:
        send_confirmation_email(instance)
        print("sent")

    if instance.is_verified:
        send_welcome_email(instance)
        print("sent")







        
       