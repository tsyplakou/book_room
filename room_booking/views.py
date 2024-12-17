from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

from room.models import Room
from .filters import BookingFilter
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation


ROOM_OPENING_TIME = 9
ROOM_CLOSING_TIME = 18


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
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

    @action(
        detail=False,
        url_path='available_hours/(?P<room>[0-9]+)/(?P<week_number>[0-9]+)',
    )
    def available_hours_for_room(self, request, room, week_number):
        room = get_object_or_404(Room, pk=room)

        start_date = datetime.fromisocalendar(
            datetime.now().year,
            int(week_number),
            1
        )
        end_date = start_date + timedelta(days=7)

        # room_bookings_on_the_week = room.bookings.filter(
        #     Q(start_dt__gte=start_date, start_dt__lte=end_date) |
        #     Q(end_dt__gte=start_date, end_dt__lte=end_date)
        # )

        available_hours = []
        for day in range(1, 8):
            date = start_date + timedelta(days=day - 1)
            if room.bookings.filter(
                start_dt__lte=date,
                end_dt__gte=date,
            ).exists():
                continue
            else:
                if date.hour >= ROOM_OPENING_TIME and date.hour < ROOM_CLOSING_TIME:
                    available_hours.append(date.strftime('%H:%M'))

        return Response(available_hours)

    @action(
        detail=True,
        methods=['post'],
    )
    def send_confirmation_mail(self, request, pk):
        booking = self.get_object()
        send_booking_confirmation.delay(
            booking.room.name,
            booking.start_dt,
            booking.end_dt,
        )
        # send_booking_confirmation.apply_async(  # countdown, eta, priority.
        #     args=(booking.room.name, booking.start_dt, booking.end_dt,),
        # )
        # send_booking_confirmation.apply(
        #     args=(booking.room.name, booking.start_dt, booking.end_dt,),
        # )
        from book_room import celery_app
        celery_app.send_task(
            'room_booking.tasks.send_booking_confirmation',
            args=(booking.room.name, booking.start_dt, booking.end_dt,),
        )
        return Response()
