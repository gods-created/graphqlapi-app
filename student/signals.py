from django.db.models.signals import post_save
from .models import Student
from django.dispatch import receiver
from loguru import logger

@receiver(post_save, sender=Student)
def new_sudent(instance, created, *args, **kwargs):
    if created:
        logger.success(
            f'Added new student with ID {instance.pk}'
        )
    
    return None