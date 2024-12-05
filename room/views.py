from rest_framework import viewsets

from book_room.cache import CacheManager, _24_HOURS
from book_room.permissions import AdminOrClientReadOnlyPermission
from .models import Room
from .serializers import (
    RoomSerializer,
    RoomListSerializer,
    RoomWithLocationSerializer,
)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('location')
    serializer_class = RoomSerializer
    permission_classes = (
        AdminOrClientReadOnlyPermission,
    )

    def get_queryset(self):
        if queryset := CacheManager().get('room_view_queryset'):
            return queryset
        else:
            queryset = super().get_queryset()
            CacheManager().set('room_view_queryset', queryset, _24_HOURS)
            return queryset

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return RoomListSerializer
        elif self.action == 'retrieve':
            return RoomWithLocationSerializer
        return self.serializer_class
