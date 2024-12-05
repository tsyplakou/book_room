from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from book_room.cache import CacheManager
from .models import Location


@receiver(post_save, sender=Location)
@receiver(post_delete, sender=Location)
def cache_location_changes(sender, instance, using, **kwargs):
    CacheManager().clear_cache('location_view_queryset')
