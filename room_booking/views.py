from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, exceptions

from .filters import BookingFilter
from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookingFilter
    serializer_class = BookingSerializer

    def get_queryset(self):
        if self.request.user.is_client:
            return self.queryset.filter(client=self.request.user)
        elif self.request.user.is_admin:
            return self.queryset

    def get_object(self):
        obj = super().get_object()

        if obj.client != self.request.user:
            raise exceptions.NotFound
        return obj
