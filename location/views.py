from rest_framework import viewsets

from book_room.cache import CacheManager, _24_HOURS
from book_room.permissions import AdminOrClientReadOnlyPermission
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    permission_classes = (
        AdminOrClientReadOnlyPermission,
    )

    def get_queryset(self):
        if queryset := CacheManager().get('location_view_queryset'):
            return queryset
        else:
            queryset = super().get_queryset()
            CacheManager().set('location_view_queryset', queryset, _24_HOURS)
            return queryset
