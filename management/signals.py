# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Notification, Booking
#
# @receiver(post_save, sender=Booking)
# def create_booking_notification(sender, instance, created, **kwargs):
#     if created:
#         Notification.objects.create(
#             user=instance.user,
#             booking=instance,
#             message=f'Your booking for {instance.item.name} on {instance.start_time} has been confirmed.'
#         )
#
# @receiver(post_save, sender=Booking)
# def update_booking_notification(sender, instance, **kwargs):
#     if instance.status == 'C':
#         Notification.objects.create(
#             user=instance.user,
#             booking=instance,
#             message=f'Your booking for {instance.item.name} on {instance.start_time} has been cancelled.'
#         )
#     elif instance.status == 'M':
#         Notification.objects.create(
#             user=instance.user,
#             booking=instance,
#             message=f'Your booking for {instance.item.name} on {instance.start_time} has been modified.'
#         )