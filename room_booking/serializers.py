from datetime import timedelta

from django.db.models import Q
from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if attrs['start_dt'] < attrs['end_dt'] + timedelta(hours=1):
            raise serializers.ValidationError('Minimal rental time is 1 hour.')

        if Booking.objects.filter(
            room=attrs['room'],
        ).filter(
            Q(
                start_dt__lte=attrs['start_dt'],
                end_dt__gte=attrs['start_dt'],
            ) | Q(
                start_dt__lte=attrs['end_dt'],
                end_dt__gte=attrs['end_dt'],
            )
        ).exists():
            raise serializers.ValidationError(
                'Room is already booked during this time.'
            )

        return attrs

    class Meta:
        model = Booking
        fields = (
            'pk',
            'start_dt',
            'end_dt',
            'room',
        )
