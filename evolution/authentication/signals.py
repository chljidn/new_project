# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from authentication.models import User, general_user
#
# @receiver(post_save, sender=User)
# def general_user_create(sender, instance, created, **kwargs):
#     if created:
#         general_user.create(user= instance)
