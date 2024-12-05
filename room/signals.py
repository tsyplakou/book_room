from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from book_room.cache import CacheManager
from .models import Room


@receiver(post_save, sender=Room)
@receiver(post_delete, sender=Room)
def cache_location_changes(sender, instance, using, **kwargs):
    CacheManager().clear_cache('room_view_queryset')
